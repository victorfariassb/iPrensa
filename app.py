import gspread
import base64
import os
import json
import pandas as pd

from flask import Flask, render_template

from conta_candidatos import contagem_candidatos

app = Flask(__name__)

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials)
spreadsheet = service_account.open_by_key(spreadsheet_id) 

worksheet = spreadsheet.worksheet('uol')
uol = pd.DataFrame(worksheet.get_all_records())

worksheet2 = spreadsheet.worksheet('globo')
globo = pd.DataFrame(worksheet2.get_all_records())

@app.route("/")
def dados_candidatos():
    palavras_uol = conta_palavras(uol)
    semana_bolso, mes_bolso, ano_bolso = contagem_candidatos('Bolsonaro', uol)
    semana_lula, mes_lula, ano_lula = contagem_candidatos('Lula', uol)
    semana_moro, mes_moro, ano_moro = contagem_candidatos('Moro', uol)
    semana_ciro, mes_ciro, ano_ciro = contagem_candidatos('Ciro', uol)
    semana_doria, mes_doria, ano_doria = contagem_candidatos('Doria', uol)
    semana_bolso_globo, mes_bolso_globo, ano_bolso_globo = contagem_candidatos('Bolsonaro', globo)
    semana_lula_globo, mes_lula_globo, ano_lula_globo = contagem_candidatos('Lula', globo)
    semana_moro_globo, mes_moro_globo, ano_moro_globo = contagem_candidatos('Moro', globo)
    semana_ciro_globo, mes_ciro_globo, ano_ciro_globo = contagem_candidatos('Ciro', globo)
    semana_doria_globo, mes_doria_globo, ano_doria_globo = contagem_candidatos('Doria', globo)
    return render_template(
        "home.html", semana_bolso=semana_bolso, mes_bolso=mes_bolso, ano_bolso=ano_bolso,
        semana_lula=semana_lula, mes_lula=mes_lula, ano_lula=ano_lula,
        semana_moro=semana_moro, mes_moro=mes_moro, ano_moro=ano_moro,
        semana_ciro=semana_ciro, mes_ciro=mes_ciro, ano_ciro=ano_ciro,
        semana_doria=semana_doria, mes_doria=mes_doria, ano_doria=ano_doria,
        palavras_uol=palavras_uol
        semana_bolso_globo=semana_bolso_globo, mes_bolso_globo=mes_bolso_globo, ano_bolso_globo=ano_bolso_globo,
        semana_lula_globo=semana_lula_globo, mes_lula_globo=mes_lula_globo, ano_lula_globo=ano_lula_globo,
        semana_moro_globo=semana_moro_globo, mes_moro_globo=mes_moro_globo, ano_moro_globo=ano_moro_globo,
        semana_ciro_globo=semana_ciro_globo, mes_ciro_globo=mes_ciro_globo, ano_ciro_globo=ano_ciro_globo,
        semana_doria_globo=semana_doria_globo, mes_doria_globo=mes_doria_globo, ano_doria_globo=ano_doria_globo)
