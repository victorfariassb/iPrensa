import base64
import gspread
import json
import pandas as pd
import os

from raspador_sites import coleta_uol
from contagem_palavras import conta_palavras

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) 
spreadsheet = service_account.open_by_key(spreadsheet_id) 

uol_sheet = spreadsheet.worksheet('uol') 
  
try:
  coleta_uol(uol_sheet)
finally:
  next

# Conta palavras 
contagem = spreadsheet.worksheet('mais_faladas') 

conta_palavras(uol_sheet, contagem)
