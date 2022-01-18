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

contagem_folha = spreadsheet.worksheet('contagem_folha')
semana_folha = contagem_folha.col_values(2)
mes_folha = contagem_folha.col_values(3)
ano_folha = contagem_folha.col_values(4)

folhab1 = semana_folha[1]
folhab2 = mes_folha[1]
folhab3 = ano_folha[1]

folhal1 = semana_folha[2]
folhal2 = mes_folha[2]
folhal3 = ano_folha[2]

folham1 = semana_folha[3]
folham2 = mes_folha[3]
folham3 = ano_folha[3]

folhac1 = semana_folha[4]
folhac2 = mes_folha[4]
folhac3 = ano_folha[4]

folhad1 = semana_folha[5]
folhad2 = mes_folha[5]
folhad3 = ano_folha[5]

# Coleta hora
oglobo = spreadsheet.worksheet('oglobo')
oglobo = pd.DataFrame(oglobo.get_all_records())
hora =oglobo['data'].iloc[-1]
hora = str(hora)

@app.route("/")
def dados_jornais():
    return render_template(
        "home.html",
        hora=hora,
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
        semana_doria_jp=jpd1, mes_doria_jp=jpd2, ano_doria_jp=jpd3,
        semana_bolso_folha=folhab1, mes_bolso_folha=folhab2, ano_bolso_folha=folhab3,
        semana_lula_folha=folhal1, mes_lula_folha=folhal2, ano_lula_folha=folhal3,
        semana_moro_folha=folham1, mes_moro_folha=folham2, ano_moro_folha=folham3,
        semana_ciro_folha=folhac1, mes_ciro_folha=folhac2, ano_ciro_folha=folhac3,
        semana_doria_folha=folhad1, mes_doria_folha=folhad2, ano_doria_folha=folhad3)


# Segunda página
contagem_palavras = spreadsheet.worksheet('mais_faladas')
globo = contagem_palavras.col_values(1)
globoq = contagem_palavras.col_values(2)
uol = contagem_palavras.col_values(3)
uolq = contagem_palavras.col_values(4)
jp = contagem_palavras.col_values(5)
jpq = contagem_palavras.col_values(6)

globo1 = globo[1]
globoq1 = globoq[1]
uol1 = uol[1]
uolq1 = uolq[1]
jp1 = jp[1]
jpq1 = jpq[1]

globo2 = globo[2]
globoq2 = globoq[2]
uolq2 = uolq[2]
uol2 = uol[2]
jp2 = jp[2]
jpq2 = jpq[2]

globo3 = globo[3]
globoq3 = globoq[3]
uolq3 = uolq[3]
uol3 = uol[3]
jp3 = jp[3]
jpq3 = jpq[3]

globo4 = globo[4]
globoq4 = globoq[4]
uolq4 = uolq[4]
uol4 = uol[4]
jp4 = jp[4]
jpq4 = jpq[4]

globo5 = globo[5]
globoq5 = globoq[5]
uolq5 = uolq[5]
uol5 = uol[5]
jp5 = jp[5]
jpq5 = jpq[5]

globo6 = globo[6]
globoq6 = globoq[6]
uolq6 = uolq[6]
uol6 = uol[6]
jp6 = jp[6]
jpq6 = jpq[6]

globo7 = globo[7]
globoq7 = globoq[7]
uolq7 = uolq[7]
uol7 = uol[7]
jp7 = jp[7]
jpq7 = jpq[7]

globo8 = globo[8]
globoq8 = globoq[8]
uolq8 = uolq[8]
uol8 = uol[8]
jp8 = jp[8]
jpq8 = jpq[8]

globo9 = globo[9]
globoq9 = globoq[9]
uolq9= uolq[9]
uol9 = uol[9]
jp9 = jp[9]
jpq9 = jpq[9]

globo10 = globo[10]
globoq10 = globoq[10]
uolq10 = uolq[10]
uol10 = uol[10]
jp10 = jp[10]
jpq10 = jpq[10]

@app.route("palavras_mais_faladas")
def termos_populares():
    return render_template(
        'termos_populares.html',
        hora=hora,
        g1=globoq1, g2=globoq2, g3=globoq3, g4=globoq4, g5=globoq5, g6=globoq6, g7=globoq7, g8=globoq8, g9=globoq9, g10=globoq10,
        w1=globo1, w2=globo2, w3=globo3, w4=globo4, w5=globo5, w6=globo6, w7=globo7, w8=globo8, w9=globo9, w10=globo10,
        u1=uolq1, u2=uolq2, u3=uolq3, u4=uolq4, u5=uolq5, u6=uolq6, u7=uolq7, u8=uolq8, u9=uolq9, u10=uolq10,
        p1=uol1, p2=uol2, p3=uol3, p4=uol4, p5=uol5, p6=uol6, p7=uol7, p8=uol8, p9=uol9, p10=uol10,
        jp_1=jpq1, jp_2=jpq2, jp_3=jpq3, jp_4=jpq4, jp_5=jpq5, jp_6=jpq6, jp_7=jpq7, jp_8=jpq8, jp_9=jpq9, jp_10=jpq10,
        jp1=jp1, jp2=jp2, jp3=jp3, jp4=jp4, jp5=jp5, jp6=jp6, jp7=jp7, jp8=jp8, jp9=jp9, jp10=jp10)

