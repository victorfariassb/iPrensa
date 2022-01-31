import base64
import gspread
import json
import pandas as pd
import os

from raspador_sites import coleta_folha, coleta_oglobo

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) 
spreadsheet = service_account.open_by_key(spreadsheet_id) 

folha_sheet = spreadsheet.worksheet('folha') 
oglobo_sheet = spreadsheet.worksheet('oglobo') 
estadao_sheet = spreadsheet.worksheet('estadao')

try:
  coleta_folha(folha_sheet)
finally:
  next
try:
  coleta_oglobo(oglobo_sheet)
finally:
  next

  try:
    coleta_estadao(estadao_sheet)
finally:
  next

# Conta palavras 
contagem = spreadsheet.worksheet('mais_faladas') 

conta_palavras(folha_sheet, contagem)
conta_palavras(oglobo_sheet, contagem)
conta_palavras(estadao_sheet, contagem)
