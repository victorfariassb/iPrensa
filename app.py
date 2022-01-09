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
p6=palavras_uol[5][0]
p7=palavras_uol[6][0]
p8=palavras_uol[7][0]
p9=palavras_uol[8][0]
p10=palavras_uol[9][0]

u1=palavras_uol[0][1] 
u2=palavras_uol[1][1]
u3=palavras_uol[2][1]
u4=palavras_uol[3][1]
u5=palavras_uol[4][1]
u6=palavras_uol[5][1] 
u7=palavras_uol[6][1] 
u8=palavras_uol[7][1] 
u9=palavras_uol[8][1] 
u10=palavras_uol[9][1] 

palavras_globo = conta_palavras(globo)
w1=palavras_globo[0][0] 
w2=palavras_globo[1][0]
w3=palavras_globo[2][0]
w4=palavras_globo[3][0]
w5=palavras_globo[4][0]
w6=palavras_globo[5][0] 
w7=palavras_globo[6][0]
w8=palavras_globo[7][0]
w9=palavras_globo[8][0]
w10=palavras_globo[9][0]

g1=palavras_globo[0][1] 
g2=palavras_globo[1][1]
g3=palavras_globo[2][1]
g4=palavras_globo[3][1]
g5=palavras_globo[4][1]
g6=palavras_globo[5][1] 
g7=palavras_globo[6][1] 
g8=palavras_globo[7][1] 
g9=palavras_globo[8][1] 
g10=palavras_globo[9][1] 

contagem_globo = spreadsheet.worksheet('contagem_globo')

gb1 = contagem_globo.acell('B2').value
gb2 = contagem_globo.acell('C2').value
gb3 = contagem_globo.acell('D2').value

gl1 = contagem_globo.acell('B3').value
gl2 = contagem_globo.acell('C3').value
gl3 = contagem_globo.acell('D3').value

gm1 = contagem_globo.acell('B4').value
gm2 = contagem_globo.acell('C4').value
gm3 = contagem_globo.acell('D4').value

gc1 = contagem_globo.acell('B5').value
gc2 = contagem_globo.acell('C5').value
gc3 = contagem_globo.acell('D5').value

gd1 = contagem_globo.acell('B6').value
gd2 = contagem_globo.acell('C6').value
gd3 = contagem_globo.acell('D6').value

contagem_uol = spreadsheet.worksheet('contagem_uol')

ub1 = contagem_uol.acell('B2').value
ub2 = contagem_uol.acell('C2').value
ub3 = contagem_uol.acell('D2').value

ul1 = contagem_uol.acell('B3').value
ul2 = contagem_uol.acell('C3').value
ul3 = contagem_uol.acell('D3').value

um1 = contagem_uol.acell('B4').value
um2 = contagem_uol.acell('C4').value
um3 = contagem_uol.acell('D4').value

uc1 = contagem_uol.acell('B5').value
uc2 = contagem_uol.acell('C5').value
uc3 = contagem_uol.acell('D5').value

ud1 = contagem_uol.acell('B6').value
ud2 = contagem_uol.acell('C6').value
ud3 = contagem_uol.acell('D6').value


@app.route("/")
def dados_candidatos():
    return render_template(
        "home.html",
        w1=w1, w2=w2, w3=w3, w4=w4, w5=w5, w6=w6, w7=w7, w8=w8, w9=w9, w10=w10,
        g1=g1, g2=g2, g3=g3, g4=g4, g5=g5, g6=g6, g7=g7, g8=g8, g9=g9, g10=g10,
        p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10,
        u1=u1, u2=u2, u3=u3, u4=u4, u5=u5, u6=u6, u7=u7, u8=u8, u9=u9, u10=u10,
        semana_bolso=ub1, mes_bolso=ub2, ano_bolso=ub3,
        semana_lula=ul1, mes_lula=ul2, ano_lula=ul3,
        semana_moro=um1, mes_moro=um2, ano_moro=um3,
        semana_ciro=uc1, mes_ciro=uc2, ano_ciro=uc3,
        semana_doria=ud1, mes_doria=ud2, ano_doria=ud3,
        semana_bolso_globo=gb1, mes_bolso_globo=gb2, ano_bolso_globo=gb3,
        semana_lula_globo=gl1, mes_lula_globo=gl2, ano_lula_globo=gl3,
        semana_moro_globo=gm1, mes_moro_globo=gm2, ano_moro_globo=gm3,
        semana_ciro_globo=gc1, mes_ciro_globo=gc2, ano_ciro_globo=gc3,
        semana_doria_globo=gd1, mes_doria_globo=gd2, ano_doria_globo=gd3)
