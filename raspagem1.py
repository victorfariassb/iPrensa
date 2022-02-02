import base64
import gspread
import json
import pandas as pd
import os

from raspador_sites import pega_editoria, pega_localizacao, pega_link, coleta_globo, ccoleta_jp, coleta_folha, coleta_oglobo
from contagem_palavras import conta_palavras

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) 
spreadsheet = service_account.open_by_key(spreadsheet_id) 

globo_sheet = spreadsheet.worksheet('globo') 
jp_sheet = spreadsheet.worksheet('jovem_pan') 

try:
  coleta_globo(globo_sheet)
finally:
  next
  
coleta_jp(jp_sheet)


# Conta palavras 
contagem = spreadsheet.worksheet('mais_faladas') 

conta_palavras(globo_sheet, contagem)
conta_palavras(jp_sheet, contagem)
