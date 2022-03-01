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
og = contagem_palavras.col_values(9)
ogq = contagem_palavras.col_values(10)
es = contagem_palavras.col_values(11)
esq = contagem_palavras.col_values(12)
cnn = contagem_palavras.col_values(13)
cnnq = contagem_palavras.col_values(14)

globo1 = globo[1]
globoq1 = globoq[1]
uol1 = uol[1]
uolq1 = uolq[1]
jp1 = jp[1]
jpq1 = jpq[1]
f1 = folha[1]
fq1 = folhaq[1]
og1 = og[1]
ogq1 = ogq[1]
es1 = es[1]
esq1 = esq[1]
cnn1 = cnn[1]
cnnq1 = cnnq[1]

globo2 = globo[2]
globoq2 = globoq[2]
uolq2 = uolq[2]
uol2 = uol[2]
jp2 = jp[2]
jpq2 = jpq[2]
f2 = folha[2]
fq2 = folhaq[2]
og2 = og[2]
ogq2 = ogq[2]
es2 = es[2]
esq2 = esq[2]
cnn2 = cnn[2]
cnnq2 = cnnq[2]


globo3 = globo[3]
globoq3 = globoq[3]
uolq3 = uolq[3]
uol3 = uol[3]
jp3 = jp[3]
jpq3 = jpq[3]
f3 = folha[3]
fq3 = folhaq[3]
og3 = og[3]
ogq3 = ogq[3]
es3 = es[3]
esq3 = esq[3]
cnn3 = cnn[3]
cnnq3 = cnnq[3]

globo4 = globo[4]
globoq4 = globoq[4]
uolq4 = uolq[4]
uol4 = uol[4]
jp4 = jp[4]
jpq4 = jpq[4]
f4 = folha[4]
fq4 = folhaq[4]
og4 = og[4]
ogq4 = ogq[4]
es4 = es[4]
esq4 = esq[4]
cnn4 = cnn[4]
cnnq4 = cnnq[4]


globo5 = globo[5]
globoq5 = globoq[5]
uolq5 = uolq[5]
uol5 = uol[5]
jp5 = jp[5]
jpq5 = jpq[5]
f5 = folha[5]
fq5 = folhaq[5]
og5 = og[5]
ogq5 = ogq[5]
es5 = es[5]
esq5 = esq[5]
cnn5 = cnn[5]
cnnq5 = cnnq[5]


globo6 = globo[6]
globoq6 = globoq[6]
uolq6 = uolq[6]
uol6 = uol[6]
jp6 = jp[6]
jpq6 = jpq[6]
f6 = folha[6]
fq6 = folhaq[6]
og6 = og[6]
ogq6 = ogq[6]
es6 = es[6]
esq6 = esq[6]
cnn6 = cnn[6]
cnnq6 = cnnq[6]


globo7 = globo[7]
globoq7 = globoq[7]
uolq7 = uolq[7]
uol7 = uol[7]
jp7 = jp[7]
jpq7 = jpq[7]
f7 = folha[7]
fq7 = folhaq[7]
og7 = og[7]
ogq7 = ogq[7]
es7 = es[7]
esq7 = esq[7]
cnn7 = cnn[7]
cnnq7 = cnnq[7]

globo8 = globo[8]
globoq8 = globoq[8]
uolq8 = uolq[8]
uol8 = uol[8]
jp8 = jp[8]
jpq8 = jpq[8]
f8 = folha[8]
fq8 = folhaq[8]
og8 = og[8]
ogq8 = ogq[8]
es8 = es[8]
esq8 = esq[8]
cnn8 = cnn[8]
cnnq8 = cnnq[8]

globo9 = globo[9]
globoq9 = globoq[9]
uolq9= uolq[9]
uol9 = uol[9]
jp9 = jp[9]
jpq9 = jpq[9]
f9 = folha[9]
fq9 = folhaq[9]
og9 = og[9]
ogq9 = ogq[9]
es9 = es[9]
esq9 = esq[9]
cnn9 = cnn[9]
cnnq9 = cnnq[9]

globo10 = globo[10]
globoq10 = globoq[10]
uolq10 = uolq[10]
uol10 = uol[10]
jp10 = jp[10]
jpq10 = jpq[10]
f10 = folha[10]
fq10 = folhaq[10]
og10 = og[10]
ogq10 = ogq[10]
es10 = es[10]
esq10 = esq[10]
cnn10 = cnn[9]
cnnq10 = cnnq[9]

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
        og1 = og1, og_1 = ogq1, es1 = es1, esq1 = esq1, og2 = og2, og_2 = ogq2, es2 = es2, esq2 = esq2, og3 = og3, og_3 = ogq3, es3 = es3, esq3 = esq3,
        og4 = og4, og_4 = ogq4, es4 = es4, esq4 = esq4, og5 = og5, og_5 = ogq5, es5 = es5, esq5 = esq5, og6 = og6, og_6 = ogq6, es6 = es6, esq6 = esq6,
        og7 = og7, og_7 = ogq7, es7 = es7, esq7 = esq7, og8 = og8, og_8 = ogq8, es8 = es8, esq8 = esq8, og9 = og9, og_9 = ogq9, es9 = es9, esq9 = esq9,
        og10 = og10, og_10 = ogq10, es10 = es10, esq10 = esq10,
        cnn_1=cnnq1, cnn_2=cnnq2, cnn_3=cnnq3, cnn_4=cnnq4, cnn_5=cnnq5, cnn_6=cnnq6, cnn_7=cnnq7, cnn_8=cnnq8, cnn_9=cnnq9, cnn_10=cnnq10,
        cnn1=cnn1, cnn2=cnn2, cnn3=cnn3, cnn4=cnn4, cnn5=cnn5, cnn6=cnn6, cnn7=cnn7, cnn8=cnn8, cnn9=cnn9, cnn10=cnn10)


palavras_dia = spreadsheet.worksheet('palavras_dia')
palavras = palavras_dia.col_values(1)
contagem = palavras_dia.col_values(2)

pa1 = palavras[1]
pa2 = palavras[2]
pa3 = palavras[3]
pa4 = palavras[4]
pa5 = palavras[5]
pa6 = palavras[6]
pa7 = palavras[7]
pa8 = palavras[8]
pa9 = palavras[9]
pa10 = palavras[10]
pa11 = palavras[11]
pa12 = palavras[12]
pa13 = palavras[13]
pa14 = palavras[14]
pa15 = palavras[15]
pa16 = palavras[16]
pa17 = palavras[17]
pa18 = palavras[18]
pa19 = palavras[19]
pa20 = palavras[20]

qu1 = contagem[1]
qu2 = contagem[2]
qu3 = contagem[3]
qu4 = contagem[4]
qu5 = contagem[5]
qu6 = contagem[6]
qu7 = contagem[7]
qu8 = contagem[8]
qu9 = contagem[9]
qu10 = contagem[10]
qu11 = contagem[11]
qu12 = contagem[12]
qu13 = contagem[13]
qu14 = contagem[14]
qu15 = contagem[15]
qu16 = contagem[16]
qu17 = contagem[17]
qu18 = contagem[18]
qu19 = contagem[19]
qu20 = contagem[20]


@app.route("/palavra_dia")
def palavra_dia():
    return render_template(
        "palavra_dia.html",
        pa1 = pa1, pa2 = pa2, pa3 = pa3, pa4 = pa4, pa5 = pa5, pa6 = pa6, pa7 = pa7, pa8 = pa8, pa9 = pa9, pa10 = pa10,
        pa11 = pa11, pa12 = pa12, pa13 = pa13, pa14 = pa14, pa15 = pa15, pa16 = pa16, pa17 = pa17, pa18 = pa18, pa19 = pa19, pa20 = pa20,
        qu1 = qu1, qu2 = qu2, qu3 = qu3, qu4 = qu4, qu5 = qu5, qu6 = qu6, qu7 = qu7, qu8 = qu8, qu9 = qu9, qu10 = qu10,
        qu11 = qu11, qu12 = qu12, qu13 = qu13, qu14 = qu14, qu15 = qu15, qu16 = qu16, qu17 = qu17, qu18 = qu18, qu19 = qu19, qu20 = qu20) 


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
ub1 = semana_candidato[10]
ub2 = mes_candidato[10]
ub3 = ano_candidato[10]

ul1 = semana_candidato[11]
ul2 = mes_candidato[11]
ul3 = ano_candidato[11]

um1 = semana_candidato[12]
um2 = mes_candidato[12]
um3 = ano_candidato[12]

uc1 = semana_candidato[13]
uc2 = mes_candidato[13]
uc3 = ano_candidato[13]

ud1 = semana_candidato[14]
ud2 = mes_candidato[14]
ud3 = ano_candidato[14]

# JP

jpb1 = semana_candidato[19]
jpb2 = mes_candidato[19]
jpb3 = ano_candidato[19]

jpl1 = semana_candidato[20]
jpl2 = mes_candidato[20]
jpl3 = ano_candidato[20]

jpm1 = semana_candidato[21]
jpm2 = mes_candidato[21]
jpm3 = ano_candidato[21]

jpc1 = semana_candidato[22]
jpc2 = mes_candidato[22]
jpc3 = ano_candidato[22]

jpd1 = semana_candidato[23]
jpd2 = mes_candidato[23]
jpd3 = ano_candidato[23]

# Folha

folhab1 = semana_candidato[28]
folhab2 = mes_candidato[28]
folhab3 = ano_candidato[28]

folhal1 = semana_candidato[29]
folhal2 = mes_candidato[29]
folhal3 = ano_candidato[29]

folham1 = semana_candidato[30]
folham2 = mes_candidato[30]
folham3 = ano_candidato[30]

folhac1 = semana_candidato[31]
folhac2 = mes_candidato[31]
folhac3 = ano_candidato[31]

folhad1 = semana_candidato[32]
folhad2 = mes_candidato[32]
folhad3 = ano_candidato[32]

# O Globo

ogb1 = semana_candidato[37]
ogb2 = mes_candidato[37]
ogb3 = ano_candidato[37]

ogl1 = semana_candidato[38]
ogl2 = mes_candidato[38]
ogl3 = ano_candidato[38]

ogm1 = semana_candidato[39]
ogm2 = mes_candidato[39]
ogm3 = ano_candidato[39]

ogc1 = semana_candidato[40]
ogc2 = mes_candidato[40]
ogc3 = ano_candidato[40]

ogd1 = semana_candidato[41]
ogd2 = mes_candidato[41]
ogd3 = ano_candidato[41]

# Estadão

esb1 = semana_candidato[46]
esb2 = mes_candidato[46]
esb3 = ano_candidato[46]

esl1 = semana_candidato[47]
esl2 = mes_candidato[47]
esl3 = ano_candidato[47]

esm1 = semana_candidato[48]
esm2 = mes_candidato[48]
esm3 = ano_candidato[48]

esc1 = semana_candidato[49]
esc2 = mes_candidato[49]
esc3 = ano_candidato[49]

esd1 = semana_candidato[50]
esd2 = mes_candidato[50]
esd3 = ano_candidato[50]

# CNN
cnnb1 = semana_candidato[57]
cnnb2 = mes_candidato[57]
cnnb3 = ano_candidato[57]

cnnl1 = semana_candidato[58]
cnnl2 = mes_candidato[58]
cnnl3 = ano_candidato[58]

cnnm1 = semana_candidato[59]
cnnm2 = mes_candidato[59]
cnnm3 = ano_candidato[59]

cnnc1 = semana_candidato[60]
cnnc2 = mes_candidato[60]
cnnc3 = ano_candidato[60]

cnnd1 = semana_candidato[61]
cnnd2 = mes_candidato[61]
cnnd3 = ano_candidato[61]




@app.route("/ranking_candidatos")
def ranking_candidatos():
    return render_template(
        "ranking_candidatos.html",
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
        semana_doria_folha=folhad1, mes_doria_folha=folhad2, ano_doria_folha=folhad3,
        semana_bolso_og=ogb1, mes_bolso_og=ogb2, ano_bolso_og=ogb3,
        semana_lula_og=ogl1, mes_lula_og=ogl2, ano_lula_og=ogl3,
        semana_moro_og=ogm1, mes_moro_og=ogm2, ano_moro_og=ogm3,
        semana_ciro_og=ogc1, mes_ciro_og=ogc2, ano_ciro_og=ogc3,
        semana_doria_og=ogd1, mes_doria_og=ogd2, ano_doria_og=ogd3,
        semana_bolso_es=esb1, mes_bolso_es=esb2, ano_bolso_es=esb3,
        semana_lula_es=esl1, mes_lula_es=esl2, ano_lula_es=esl3,
        semana_moro_es=esm1, mes_moro_es=esm2, ano_moro_es=esm3,
        semana_ciro_es=esc1, mes_ciro_es=esc2, ano_ciro_es=esc3,
        semana_doria_es=esd1, mes_doria_es=esd2, ano_doria_es=esd3,
        semana_bolso_cnn=cnnb1, mes_bolso_cnn=cnnb2, ano_bolso_cnn=cnnb3,
        semana_lula_cnn=cnnl1, mes_lula_cnn=cnnl2, ano_lula_cnn=cnnl3,
        semana_moro_cnn=cnnm1, mes_moro_cnn=cnnm2, ano_moro_cnn=cnnm3,
        semana_ciro_cnn=cnnc1, mes_ciro_cnn=cnnc2, ano_ciro_cnn=cnnc3,
        semana_doria_cnn=cnnd1, mes_doria_cnn=cnnd2, ano_doria_cnn=cnnd3
        
    )
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
        
