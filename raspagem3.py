import base64
import gspread
import json
import pandas as pd
import os
import time

from contagem_candidatos import contagem_candidatos
from raspador_sites import coleta_uol
from contagem_palavras import conta_palavras

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) 
spreadsheet = service_account.open_by_key(spreadsheet_id) 

uol_sheet = spreadsheet.worksheet('uol') 


# Conta palavras 
contagem = spreadsheet.worksheet('mais_faladas') 

conta_palavras(uol_sheet, contagem)

# Conta candidatos
contagem_candidato = spreadsheet.worksheet('contagem_candidato')

jp_sheet = spreadsheet.worksheet('jovem_pan')
globo_sheet = spreadsheet.worksheet('globo')
folha_sheet = spreadsheet.worksheet('folha') 
oglobo_sheet = spreadsheet.worksheet('oglobo') 
estadao_sheet = spreadsheet.worksheet('estadao')

time.sleep(60)
contagem_candidatos(globo_sheet, contagem_candidato)
contagem_candidatos(jp_sheet, contagem_candidato)
contagem_candidatos(folha_sheet, contagem_candidato)
contagem_candidatos(oglobo_sheet, contagem_candidato)
contagem_candidatos(estadao_sheet, contagem_candidato)
contagem_candidatos(uol_sheet, contagem_candidato)
time.sleep(60)
# Raspa os dados
try:
  coleta_uol(uol_sheet)
finally:
  next


