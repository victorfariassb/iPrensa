import base64
import gspread
import json
import pandas as pd
import os

from raspador_sites import pega_editoria_globo, pega_localizacao, pega_link, coleta_globo, coleta_jp
from contagem_palavras import conta_palavras

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) 
spreadsheet = service_account.open_by_key(spreadsheet_id) 

globo_sheet = spreadsheet.worksheet('globo') 
jp_sheet = spreadsheet.worksheet('jovem_pan') 

# Raspa os dados
try:
  coleta_globo(globo_sheet)
except:
  pass
try:
  coleta_jp(jp_sheet)
except:
  pass

folha_sheet = spreadsheet.worksheet('folha') 
estadao_sheet = spreadsheet.worksheet('estadao')

# Raspagem de dados

try:
  coleta_folha(folha_sheet)
except:
  pass

try:
  coleta_estadao(estadao_sheet)
except:
  pass

uol_sheet = spreadsheet.worksheet('uol') 
cnn_sheet = spreadsheet.worksheet('cnn') 


# Raspa os dados
try:
  coleta_uol(uol_sheet)
except:
  pass

try:
  coleta_cnn(cnn_sheet)
except:
  pass