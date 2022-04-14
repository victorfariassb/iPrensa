import base64
import gspread
import json
import pandas as pd
import os
import time

from contagem_palavras import conta_palavras
from contagem_candidatos import contagem_candidatos

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) 
spreadsheet = service_account.open_by_key(spreadsheet_id) 

globo_sheet = spreadsheet.worksheet('globo') 
jp_sheet = spreadsheet.worksheet('jovem_pan') 
folha_sheet = spreadsheet.worksheet('folha') 
oglobo_sheet = spreadsheet.worksheet('oglobo') 
estadao_sheet = spreadsheet.worksheet('estadao')
uol_sheet = spreadsheet.worksheet('uol') 
cnn_sheet = spreadsheet.worksheet('cnn') 

# Conta palavras 
contagem = spreadsheet.worksheet('mais_faladas') 

conta_palavras(globo_sheet, contagem)
conta_palavras(jp_sheet, contagem)
conta_palavras(oglobo_sheet, contagem)
conta_palavras(estadao_sheet, contagem)
conta_palavras(uol_sheet, contagem)
conta_palavras(folha_sheet, contagem)
conta_palavras(cnn_sheet, contagem)

time.sleep(70)

# Conta candidatos
contagem_candidato = spreadsheet.worksheet('contagem_candidato')

contagem_candidatos(globo_sheet, contagem_candidato)
contagem_candidatos(jp_sheet, contagem_candidato)
contagem_candidatos(folha_sheet, contagem_candidato)
contagem_candidatos(oglobo_sheet, contagem_candidato)
contagem_candidatos(estadao_sheet, contagem_candidato)
contagem_candidatos(uol_sheet, contagem_candidato)
contagem_candidatos(cnn_sheet, contagem_candidato)
