import spacy
import pt_core_news_sm
from collections import Counter, OrderedDict
import gspread
import base64
import os
import json
import pandas as pd
import datetime
import numpy as np


spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials)
spreadsheet = service_account.open_by_key(spreadsheet_id) 

df = spreadsheet.worksheet('globo')
entidades = spreadsheet.worksheet('entidades')

nlp = pt_core_news_sm.load()

def conta_entidade(df, entidades):
  hoje = datetime.datetime.now()
  semana = hoje - datetime.timedelta(days=7, hours=3)
  semana = np.datetime64(semana)
      
  df = pd.DataFrame(df.get_all_records())
  df['data'] = pd.to_datetime(df['data'])
  
  df_semana = df[df['data'] >= semana]
  
  df_semana = df_semana['titulo']
  
  text = ' '.join(df_semana)

  doc = nlp(text)

  labels = [x.text for x in doc.ents]
  dicionario = Counter(labels)

  palavras = [palavra for palavra, contagem in dicionátio.most_common(10)]
  entidades.append_row([palavras])
 
conta_entidade(df, entidades)
