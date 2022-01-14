import gspread
import base64
import os
import json
import pandas as pd

from flask import Flask, render_template

app = Flask(__name__)

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials)
spreadsheet = service_account.open_by_key(spreadsheet_id) 

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

contagem_palavras = spreadsheet.worksheet('mais_faladas')
globo = contagem_palavras.row_values(2)
uol = contagem_palavras.row_values(3)
jp = contagem_palavras.row_values(4)

globo1 = globo[1]
uol1 = uol[1]
jp1 = jp[1]

globo2 = globo[2]
uol2 = uol[2]
jp2 = jp[2]

globo3 = globo[3]
uol3 = uol[3]
jp3 = jp[3]

globo4 = globo[4]
uol4 = uol[4]
jp4 = jp[4]

globo5 = globo[5]
uol5 = uol[5]
jp5 = jp[5]

globo6 = globo[6]
uol6 = uol[6]
jp6 = jp[6]

globo7 = globo[7]
uol7 = uol[7]
jp7 = jp[7]

globo8 = globo[8]
uol8 = uol[8]
jp8 = jp[8]

globo9 = globo[9]
uol9 = uol[9]
jp9 = jp[9]

globo10 = globo[10]
uol10 = uol[10]
jp10 = jp[10]

globo11 = globo[11]
uol11 = uol[11]
jp11 = jp[11]

globo12 = globo[12]
uol12 = uol[12]
jp12 = jp[12]

globo13 = globo[13]
uol13 = uol[13]
jp13 = jp[13]

globo14 = globo[14]
uol14 = uol[14]
jp14 = jp[14]

globo15 = globo[15]
uol15 = uol[15]
jp15 = jp[15]

globo16 = globo[16]
uol16 = uol[16]
jp16 = jp[16]

globo17 = globo[17]
uol17 = uol[17]
jp17 = jp[17]

globo18 = globo[18]
uol18 = uol[18]
jp18 = jp[18]

globo19 = globo[19]
uol19 = uol[19]
jp19 = jp[19]

globo20 = globo[20]
uol20 = uol[20]
jp20 = jp[20]

hora =jp['data'].iloc[-1]
hora = str(hora)

@app.route("/")
def dados_candidatos():
    return render_template(
        "home.html",
        hora=hora,
        w1=globo2, w2=globo4, w3=globo6, w4=globo8, w5=globo10, w6=globo12, w7=globo14, w8=globo16, w9=globo18, w10=globo20,
        g1=globo1, g2=globo3, g3=globo5, g4=globo7, g5=globo9, g6=globo11, g7=globo13, g8=globo15, g9=globo17, g10=globo19,
        p1=uol2, p2=uol4, p3=uol6, p4=uol8, p5=uol10, p6=uol12, p7=uol14, p8=uol16, p9=uol18, p10=uol20,
        u1=uol1, u2=uol3, u3=uol5, u4=uol7, u5=uol9, u6=uol11, u7=uol13, u8=uol15, u9=uol17, u10=uol19,
        jp1=jp2, jp2=jp4, jp3=jp6, jp4=jp8, jp5=jp10, jp6=jp12, jp7=jp14, jp8=jp16, jp9=jp18, jp10=jp20,
        jp_1=jp1, jp_2=jp3, jp_3=jp5, jp_4=jp7, jp_5=jp9, jp_6=jp11, jp_7=jp13, jp_8=jp15, jp_9=jp17, jp_10=jp19,
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
