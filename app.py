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

# Coleta 
cnn = spreadsheet.worksheet('cnn')
cnn = pd.DataFrame(cnn.get_all_records())
hora = cnn['data'].iloc[-1]
hora = str(hora)

palavras_dia = spreadsheet.worksheet('palavras_dia')
palavras = palavras_dia.col_values(1)
contagem = palavras_dia.col_values(2)

palavras_dia = pd.DataFrame(list(zip(palavras, contagem)))

contagem_palavras = spreadsheet.worksheet('mais_faladas')
total_materias = contagem_palavras.col_values(14)[1]
total_materias = "{:,}".format(int(total_materias)).replace(',','.')

ranking = spreadsheet.worksheet('ranking_times')
times_nome = ranking.col_values(1)[1:]
times_qtd = ranking.col_values(4)[1:]

palavra_do_dia = palavras[1]

times_dados = pd.DataFrame(list(zip(times_nome, times_qtd)), columns=['time', 'quantidade'])
times_dados.quantidade = times_dados.quantidade.astype(int)
times_dados = times_dados.sort_values('quantidade', ascending=False).head(11)

ranking_candidatos = spreadsheet.worksheet('contagem_candidato')
candidatos = ranking_candidatos.col_values(2)[25:]
quantidade_ultima_semana = ranking_candidatos.col_values(3)[25:]
quantidade_total_candidatos = ranking_candidatos.col_values(5)[25:]

ranking_candidatos = pd.DataFrame(list(zip(candidatos, quantidade_ultima_semana, quantidade_total_candidatos)), columns=['candidato', 'quantidade_ultima_semana', 'quantidade_total_candidatos'], dtype={'quantidade_total_candidatos': int})
ranking_candidatos = ranking_candidatos.sort_values('quantidade_total_candidatos', ascending=False)



@app.route("/")
def new_home():
    return render_template(
        "home.html", palavra_dia=palavra_do_dia, total_materias=total_materias, times_dados=times_dados, hora=hora, ranking_candidatos=ranking_candidatos, palavras=json.dumps(palavras[1:], ensure_ascii=False))
