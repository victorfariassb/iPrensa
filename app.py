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



@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
        
