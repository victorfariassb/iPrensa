import base64
import gspread
import json
import pandas as pd
import os

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

contagem_candidatos(uol_sheet, contagem_candidato)

# Raspa os dados
try:
  coleta_uol(uol_sheet)
finally:
  next


