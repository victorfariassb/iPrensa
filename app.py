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


contagem_palavras = spreadsheet.worksheet('mais_faladas')
globo = contagem_palavras.col_values(1)
globoq = contagem_palavras.col_values(2)
uol = contagem_palavras.col_values(3)
uolq = contagem_palavras.col_values(4)
jp = contagem_palavras.col_values(5)
jpq = contagem_palavras.col_values(6)
folha = contagem_palavras.col_values(7)
folhaq = contagem_palavras.col_values(8)

globo1 = globo[1]
globoq1 = globoq[1]
uol1 = uol[1]
uolq1 = uolq[1]
jp1 = jp[1]
jpq1 = jpq[1]
f1 = folha[1]
fq1 = folhaq[1]

globo2 = globo[2]
globoq2 = globoq[2]
uolq2 = uolq[2]
uol2 = uol[2]
jp2 = jp[2]
jpq2 = jpq[2]
f2 = folha[2]
fq2 = folhaq[2]

globo3 = globo[3]
globoq3 = globoq[3]
uolq3 = uolq[3]
uol3 = uol[3]
jp3 = jp[3]
jpq3 = jpq[3]
f3 = folha[3]
fq3 = folhaq[3]

globo4 = globo[4]
globoq4 = globoq[4]
uolq4 = uolq[4]
uol4 = uol[4]
jp4 = jp[4]
jpq4 = jpq[4]
f4 = folha[4]
fq4 = folhaq[4]

globo5 = globo[5]
globoq5 = globoq[5]
uolq5 = uolq[5]
uol5 = uol[5]
jp5 = jp[5]
jpq5 = jpq[5]
f5 = folha[5]
fq5 = folhaq[5]

globo6 = globo[6]
globoq6 = globoq[6]
uolq6 = uolq[6]
uol6 = uol[6]
jp6 = jp[6]
jpq6 = jpq[6]
f6 = folha[6]
fq6 = folhaq[6]

globo7 = globo[7]
globoq7 = globoq[7]
uolq7 = uolq[7]
uol7 = uol[7]
jp7 = jp[7]
jpq7 = jpq[7]
f7 = folha[7]
fq7 = folhaq[7]

globo8 = globo[8]
globoq8 = globoq[8]
uolq8 = uolq[8]
uol8 = uol[8]
jp8 = jp[8]
jpq8 = jpq[8]
f8 = folha[8]
fq8 = folhaq[8]

globo9 = globo[9]
globoq9 = globoq[9]
uolq9= uolq[9]
uol9 = uol[9]
jp9 = jp[9]
jpq9 = jpq[9]
f9 = folha[9]
fq9 = folhaq[9]

globo10 = globo[10]
globoq10 = globoq[10]
uolq10 = uolq[10]
uol10 = uol[10]
jp10 = jp[10]
jpq10 = jpq[10]
f10 = folha[10]
fq10 = folhaq[10]

contagem_candidatos = spreadsheet.worksheet('contagem_candidato')
semana_candidato = contagem_candidatos.col_values(3)
mes_candidato = contagem_candidatos.col_values(4)
ano_candidato = contagem_candidatos.col_values(5)

gb1 = semana_candidato[1]
gb2 = mes_candidato[1]
gb3 = ano_candidato[1]

gl1 = semana_candidato[2]
gl2 = mes_candidato[2]
gl3 = ano_candidato[2]

gm1 = semana_candidato[3]
gm2 = mes_candidato[3]
gm3 = ano_candidato[3]

gc1 = semana_candidato[4]
gc2 = mes_candidato[4]
gc3 = ano_candidato[4]

gd1 = semana_candidato[5]
gd2 = mes_candidato[5]
gd3 = ano_candidato[5]

# Uol
ub1 = semana_candidato[9]
ub2 = mes_candidato[9]
ub3 = ano_candidato[9]

ul1 = semana_candidato[10]
ul2 = mes_candidato[10]
ul3 = ano_candidato[10]

um1 = semana_candidato[11]
um2 = mes_candidato[11]
um3 = ano_candidato[11]

uc1 = semana_candidato[12]
uc2 = mes_candidato[12]
uc3 = ano_candidato[12]

ud1 = semana_candidato[13]
ud2 = mes_candidato[13]
ud3 = ano_candidato[13]

# JP

jpb1 = semana_candidato[17]
jpb2 = mes_candidato[17]
jpb3 = ano_candidato[17]

jpl1 = semana_candidato[18]
jpl2 = mes_candidato[18]
jpl3 = ano_candidato[18]

jpm1 = semana_candidato[19]
jpm2 = mes_candidato[19]
jpm3 = ano_candidato[19]

jpc1 = semana_candidato[20]
jpc2 = mes_candidato[20]
jpc3 = ano_candidato[20]

jpd1 = semana_candidato[21]
jpd2 = mes_candidato[21]
jpd3 = ano_candidato[21]

# Folha

folhab1 = semana_candidato[25]
folhab2 = mes_candidato[25]
folhab3 = ano_candidato[25]

folhal1 = semana_candidato[26]
folhal2 = mes_candidato[26]
folhal3 = ano_candidato[26]

folham1 = semana_candidato[27]
folham2 = mes_candidato[27]
folham3 = ano_candidato[27]

folhac1 = semana_candidato[28]
folhac2 = mes_candidato[28]
folhac3 = ano_candidato[28]

folhad1 = semana_candidato[29]
folhad2 = mes_candidato[29]
folhad3 = ano_candidato[29]

# O Globo

ogb1 = semana_candidato[34]
ogb2 = mes_candidato[34]
ogb3 = ano_candidato[34]

ogl1 = semana_candidato[35]
ogl2 = mes_candidato[35]
ogl3 = ano_candidato[35]

ogm1 = semana_candidato[36]
ogm2 = mes_candidato[36]
ogm3 = ano_candidato[36]

ogc1 = semana_candidato[37]
ogc2 = mes_candidato[37]
ogc3 = ano_candidato[37]

ogd1 = semana_candidato[38]
ogd2 = mes_candidato[38]
ogd3 = ano_candidato[38]


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
        g1=globoq1, g2=globoq2, g3=globoq3, g4=globoq4, g5=globoq5, g6=globoq6, g7=globoq7, g8=globoq8, g9=globoq9, g10=globoq10,
        w1=globo1, w2=globo2, w3=globo3, w4=globo4, w5=globo5, w6=globo6, w7=globo7, w8=globo8, w9=globo9, w10=globo10,
        u1=uolq1, u2=uolq2, u3=uolq3, u4=uolq4, u5=uolq5, u6=uolq6, u7=uolq7, u8=uolq8, u9=uolq9, u10=uolq10,
        p1=uol1, p2=uol2, p3=uol3, p4=uol4, p5=uol5, p6=uol6, p7=uol7, p8=uol8, p9=uol9, p10=uol10,
        jp_1=jpq1, jp_2=jpq2, jp_3=jpq3, jp_4=jpq4, jp_5=jpq5, jp_6=jpq6, jp_7=jpq7, jp_8=jpq8, jp_9=jpq9, jp_10=jpq10,
        jp1=jp1, jp2=jp2, jp3=jp3, jp4=jp4, jp5=jp5, jp6=jp6, jp7=jp7, jp8=jp8, jp9=jp9, jp10=jp10,
        f1 = f1, f2=f2, f3=f3, f4=f4, f5=f5, f6=f6, f7=f7, f8=f8, f9=f9, f10=f10,
        fq1 = fq1, fq2=fq2, fq3=fq3, fq4=fq4, fq5=fq5, fq6=fq6, fq7=fq7, fq8=fq8, fq9=fq9, fq10=fq10,
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
        semana_doria_folha=folhad1, mes_doria_folha=folhad2, ano_doria_folha=folhad3,
        semana_bolso_og=ogb1, mes_bolso_og=ogb2, ano_bolso_og=ogb3,
        semana_lula_og=ogl1, mes_lula_og=ogl2, ano_lula_og=ogl3,
        semana_moro_og=ogm1, mes_moro_og=ogm2, ano_moro_og=ogm3,
        semana_ciro_og=ogc1, mes_ciro_og=ogc2, ano_ciro_og=ogc3,
        semana_doria_og=ogd1, mes_doria_og=ogd2, ano_doria_og=ogd3)
