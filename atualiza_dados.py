import base64
import gspread
import json
import pandas as pd
import os
import time

from contagem_palavras import conta_palavras
from contagem_candidatos import contagem_candidatos
from termos_dia import termos_dia
from ranking_times import ranking_times

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) 
spreadsheet = service_account.open_by_key(spreadsheet_id) 

globo_sheet = spreadsheet.worksheet('globo') 
jp_sheet = spreadsheet.worksheet('jovem_pan') 
folha_sheet = spreadsheet.worksheet('folha') 
estadao_sheet = spreadsheet.worksheet('estadao')
uol_sheet = spreadsheet.worksheet('uol') 
cnn_sheet = spreadsheet.worksheet('cnn') 

# Conta palavras 
contagem = spreadsheet.worksheet('mais_faladas') 

conta_palavras(globo_sheet, contagem)
conta_palavras(jp_sheet, contagem)
conta_palavras(estadao_sheet, contagem)

time.sleep(20)

conta_palavras(uol_sheet, contagem)
conta_palavras(folha_sheet, contagem)
conta_palavras(cnn_sheet, contagem)

time.sleep(20)

# Conta candidatos
contagem_candidato = spreadsheet.worksheet('contagem_candidato')

contagem_candidatos(globo_sheet, contagem_candidato)
contagem_candidatos(jp_sheet, contagem_candidato)
contagem_candidatos(folha_sheet, contagem_candidato)
contagem_candidatos(estadao_sheet, contagem_candidato)
contagem_candidatos(uol_sheet, contagem_candidato)
contagem_candidatos(cnn_sheet, contagem_candidato)

time.sleep(20)

# Termos do dia
palavras_dia = spreadsheet.worksheet('palavras_dia') 
termos_dia(palavras_dia)

# Ranking dos times
ranking = spreadsheet.worksheet('ranking_times')
ranking_times(globo_sheet, uol_sheet, ranking)

