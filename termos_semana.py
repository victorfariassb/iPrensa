import base64
import datetime
import gspread
import json
import numpy as np
import pandas as pd
import spacy.attrs
import os
from collections import Counter


nlp = spacy.load('pt_core_news_sm')

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) 
spreadsheet = service_account.open_by_key(spreadsheet_id) 

palavra_semana = spreadsheet.worksheet('palavra_semana') 
globo_sheet = spreadsheet.worksheet('globo') 
uol_sheet = spreadsheet.worksheet('uol') 
jp_sheet = spreadsheet.worksheet('jovem_pan') 
folha_sheet = spreadsheet.worksheet('folha') 
oglobo_sheet = spreadsheet.worksheet('oglobo') 


def termo_semana(contagem):
    linha = 2
    coluna = 2
    jornais = [globo_sheet, uol_sheet, jp_sheet, folha_sheet, oglobo_sheet]

    tabelas = []
    for jornal in jornais:
        # baixar e converter os dados
        df = pd.DataFrame(jornal.get_all_records())
        tabelas.append(df)
    dados = pd.concat(tabelas).reset_index()

    # Filtro da data
    hoje = datetime.datetime.now()
    semana = hoje - datetime.timedelta(days=7, hours=3)
    semana = np.datetime64(semana)

    dados['data'] = pd.to_datetime(dados['data'])

    df_semana = dados[dados['data'] >= semana]

    # Filtro da relevância
    df_semana['materia'] = pd.to_numeric(df_semana['materia'])
    df_semana = df_semana[df_semana['materia'] < 21]
    df_semana = df_semana['titulo'].drop_duplicates()

    # Contagem de termos
    text = ' '.join(df_semana)

    doc = nlp(text)

    labels = [x.text for x in doc.ents]
    dicionario = Counter(labels)

    palavras = [palavra for palavra in dicionario.most_common(10)]
    for palavra in palavras:
        contagem.update_cell(linha, coluna, palavra[0])
        contagem.update_cell(linha, coluna + 1, palavra[1])
        linha += 2
        coluna = 1

termo_semana(palavra_semana)
