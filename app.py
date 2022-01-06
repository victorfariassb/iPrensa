import gspread
import base64
import os
import json
import pandas as pd

from flask import Flask, render_template

from conta_candidatos import contagem_candidatos
from contagem_palavras import conta_palavras

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

palavras_uol = conta_palavras(uol)
p1=palavras_uol[0][0] 
p2=palavras_uol[1][0]
p3=palavras_uol[2][0]
p4=palavras_uol[3][0]
p5=palavras_uol[4][0]

u1=palavras_uol[0][1] 
u2=palavras_uol[1][1]
u3=palavras_uol[2][1]
u4=palavras_uol[3][1]
u5=palavras_uol[4][1]

palavras_globo = conta_palavras(globo)
w1=palavras_globo[0][0] 
w2=palavras_globo[1][0]
w3=palavras_globo[2][0]
w4=palavras_globo[3][0]
w5=palavras_globo[4][0]

g1=palavras_globo[0][1] 
g2=palavras_globo[1][1]
g3=palavras_globo[2][1]
g4=palavras_globo[3][1]
g5=palavras_globo[4][1]


@app.route("/")
def dados_candidatos():
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
        w1=w1, w2=w2, w3=w3, w4=w4, w5=w5, g1=g1, g2=g2, g3=g3, g4=g4, g5=g5, p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, u1=u1, u2=u2, u3=u3, u4=u4, u5=u5,
        semana_bolso_globo=semana_bolso_globo, mes_bolso_globo=mes_bolso_globo, ano_bolso_globo=ano_bolso_globo,
        semana_lula_globo=semana_lula_globo, mes_lula_globo=mes_lula_globo, ano_lula_globo=ano_lula_globo,
        semana_moro_globo=semana_moro_globo, mes_moro_globo=mes_moro_globo, ano_moro_globo=ano_moro_globo,
        semana_ciro_globo=semana_ciro_globo, mes_ciro_globo=mes_ciro_globo, ano_ciro_globo=ano_ciro_globo,
        semana_doria_globo=semana_doria_globo, mes_doria_globo=mes_doria_globo, ano_doria_globo=ano_doria_globo)
