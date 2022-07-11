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
# vamos criar um df com os dados das 4 primeiras listas para adicionar no flask
globo_uol = pd.DataFrame(list(zip(globo, globoq, uol, uolq)))

jp = contagem_palavras.col_values(5)
jpq = contagem_palavras.col_values(6)
folha = contagem_palavras.col_values(7)
folhaq = contagem_palavras.col_values(8)

folha_jp = pd.DataFrame(list(zip(jp, jpq, folha, folhaq)))

es = contagem_palavras.col_values(9)
esq = contagem_palavras.col_values(10)
cnn = contagem_palavras.col_values(11)
cnnq = contagem_palavras.col_values(12)

estadao_cnn = pd.DataFrame(list(zip(es, esq, cnn, cnnq)))

# Coleta 
cnn = spreadsheet.worksheet('cnn')
cnn = pd.DataFrame(cnn.get_all_records())
hora = cnn['data'].iloc[-1]
hora = str(hora)


@app.route("/")
def dados_jornais():
    return render_template(
        "home.html",
        hora=hora, globo_uol=globo_uol, folha_jp=folha_jp, estadao_cnn=estadao_cnn)


palavras_dia = spreadsheet.worksheet('palavras_dia')
palavras = palavras_dia.col_values(1)
contagem = palavras_dia.col_values(2)

palavras_dia = pd.DataFrame(list(zip(palavras, contagem)))



@app.route("/palavra_dia")
def palavra_dia():
    return render_template(
        "palavra_dia.html", palavras_dia=palavras_dia) 


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

# Estadão

esb1 = semana_candidato[37]
esb2 = mes_candidato[37]
esb3 = ano_candidato[37]

esl1 = semana_candidato[38]
esl2 = mes_candidato[38]
esl3 = ano_candidato[38]

esm1 = semana_candidato[39]
esm2 = mes_candidato[39]
esm3 = ano_candidato[39]

esc1 = semana_candidato[40]
esc2 = mes_candidato[40]
esc3 = ano_candidato[40]

esd1 = semana_candidato[41]
esd2 = mes_candidato[41]
esd3 = ano_candidato[41]

# CNN
cnnb1 = semana_candidato[46]
cnnb2 = mes_candidato[46]
cnnb3 = ano_candidato[46]

cnnl1 = semana_candidato[47]
cnnl2 = mes_candidato[47]
cnnl3 = ano_candidato[47]

cnnm1 = semana_candidato[48]
cnnm2 = mes_candidato[48]
cnnm3 = ano_candidato[48]

cnnc1 = semana_candidato[49]
cnnc2 = mes_candidato[49]
cnnc3 = ano_candidato[49]

cnnd1 = semana_candidato[50]
cnnd2 = mes_candidato[50]
cnnd3 = ano_candidato[50]




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
        
