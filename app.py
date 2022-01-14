import gspread
import base64
import os
import json
import pandas as pd

from flask import Flask, render_template

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

worksheet2 = spreadsheet.worksheet('globo')
globo = pd.DataFrame(worksheet2.get_all_records())

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

worksheet3 = spreadsheet.worksheet('jovem_pan')
jp = pd.DataFrame(worksheet3.get_all_records())

palavras_jp = conta_palavras(jp)
jp1 = palavras_jp[0][0]
jp2 = palavras_jp[1][0]
jp3 = palavras_jp[2][0]
jp4 = palavras_jp[3][0]
jp5 = palavras_jp[4][0]
jp6 = palavras_jp[5][0]
jp7 = palavras_jp[6][0]
jp8 = palavras_jp[7][0]
jp9 = palavras_jp[8][0]
jp10 = palavras_jp[9][0]

jp_1 = palavras_jp[0][1]
jp_2 = palavras_jp[1][1]
jp_3 = palavras_jp[2][1]
jp_4 = palavras_jp[3][1]
jp_5 = palavras_jp[4][1]
jp_6 = palavras_jp[5][1]
jp_7 = palavras_jp[6][1]
jp_8 = palavras_jp[7][1]
jp_9 = palavras_jp[8][1]
jp_10 = palavras_jp[9][1]

contagem_globo = spreadsheet.worksheet('contagem_globo')
semana_globo = contagem_globo.col_values(2)
mes_globo = contagem_globo.col_values(3)
ano_globo = contagem_globo.col_values(4)

gb1 = semana_globo[1]
gb2 = mes_globo[1]
gb3 = ano_globo[1]

gl1 = semana_globo[2]
gl2 = mes_globo[2]
gl3 = ano_globo[2]

gm1 = semana_globo[3]
gm2 = mes_globo[3]
gm3 = ano_globo[3]

gc1 = semana_globo[4]
gc2 = mes_globo[4]
gc3 = ano_globo[4]

gd1 = semana_globo[5]
gd2 = mes_globo[5]
gd3 = ano_globo[5]

contagem_uol = spreadsheet.worksheet('contagem_uol')
semana_uol = contagem_uol.col_values(2)
mes_uol = contagem_uol.col_values(3)
ano_uol = contagem_uol.col_values(4)

ub1 = semana_uol[1]
ub2 = mes_uol[1]
ub3 = ano_uol[1]

ul1 = semana_uol[2]
ul2 = mes_uol[2]
ul3 = ano_uol[2]

um1 = semana_uol[3]
um2 = mes_uol[3]
um3 = ano_uol[3]

uc1 = semana_uol[4]
uc2 = mes_uol[4]
uc3 = ano_uol[4]

ud1 = semana_uol[5]
ud2 = mes_uol[5]
ud3 = ano_uol[5]

contagem_jp = spreadsheet.worksheet('contagem_jp')
semana_jp = contagem_jp.col_values(2)
mes_jp = contagem_jp.col_values(3)
ano_jp = contagem_jp.col_values(4)

jpb1 = semana_jp[1]
jpb2 = mes_jp[1]
jpb3 = ano_jp[1]

jpl1 = semana_jp[2]
jpl2 = mes_jp[2]
jpl3 = ano_jp[2]

jpm1 = semana_jp[3]
jpm2 = mes_jp[3]
jpm3 = ano_jp[3]

jpc1 = semana_jp[4]
jpc2 = mes_jp[4]
jpc3 = ano_jp[4]

jpd1 = semana_jp[5]
jpd2 = mes_jp[5]
jpd3 = ano_jp[5]


hora = jp['data'].iloc[-1]

@app.route("/")
def dados_candidatos():
    return render_template(
        "home.html",
        hora=hora,
        w1=w1, w2=w2, w3=w3, w4=w4, w5=w5, w6=w6, w7=w7, w8=w8, w9=w9, w10=w10,
        g1=g1, g2=g2, g3=g3, g4=g4, g5=g5, g6=g6, g7=g7, g8=g8, g9=g9, g10=g10,
        p1=p1, p2=p2, p3=p3, p4=p4, p5=p5, p6=p6, p7=p7, p8=p8, p9=p9, p10=p10,
        u1=u1, u2=u2, u3=u3, u4=u4, u5=u5, u6=u6, u7=u7, u8=u8, u9=u9, u10=u10,
        jp1=jp1, jp2=jp2, jp3=jp3, jp4=jp4, jp5=jp5, jp6=jp6, jp7=jp7, jp8=jp8, jp9=jp9, jp10=jp10,
        jp_1=jp_1, jp_2=jp_2, jp_3=jp_3, jp_4=jp_4, jp_5=jp_5, jp_6=jp_6, jp_7=jp_7, jp_8=jp_8, jp_9=jp_9, jp_10=jp_10,
        semana_bolso=ub1, mes_bolso=ub2, ano_bolso=ub3,
        semana_lula=ul1, mes_lula=ul2, ano_lula=ul3,
        semana_moro=um1, mes_moro=um2, ano_moro=um3,
        semana_ciro=uc1, mes_ciro=uc2, ano_ciro=uc3,
        semana_doria=ud1, mes_doria=ud2, ano_doria=ud3,
        semana_bolso_globo=gb1, mes_bolso_globo=gb2, ano_bolso_globo=gb3,
        semana_lula_globo=gl1, mes_lula_globo=gl2, ano_lula_globo=gl3,
        semana_moro_globo=gm1, mes_moro_globo=gm2, ano_moro_globo=gm3,
        semana_ciro_globo=gc1, mes_ciro_globo=gc2, ano_ciro_globo=gc3,
        semana_doria_globo=gd1, mes_doria_globo=gd2, ano_doria_globo=gd3,
        semana_bolso_jp=jpb1, mes_bolso_jp=jpb2, ano_bolso_jp=jpb3,
        semana_lula_jp=jpl1, mes_lula_jp=jpl2, ano_lula_jp=jpl3,
        semana_moro_jp=jpm1, mes_moro_jp=jpm2, ano_moro_jp=jpm3,
        semana_ciro_jp=jpc1, mes_ciro_jp=jpc2, ano_ciro_jp=jpc3,
        semana_doria_jp=jpd1, mes_doria_jp=jpd2, ano_doria_jp=jpd3)
