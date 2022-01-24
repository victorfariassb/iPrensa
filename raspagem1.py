import base64
import gspread
import json
import pandas as pd

from raspador_sites import pega_editoria, pega_localizacao, pega_link, coleta_globo, coleta_uol, coleta_jp, coleta_folha, coleta_oglobo

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) 
spreadsheet = service_account.open_by_key(spreadsheet_id) 

globo_sheet = spreadsheet.worksheet('globo') 
uol_sheet = spreadsheet.worksheet('uol') 
jp_sheet = spreadsheet.worksheet('jovem_pan') 

try:
  coleta_globo()
finally:
  next
  
try:
  coleta_uol()
finally:
  next

coleta_jp()
