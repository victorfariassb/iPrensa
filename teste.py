import base64
import gspread
import json
import pandas as pd
import os

from contagem_palavras import conta_palavras

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) # autenticação
spreadsheet = service_account.open_by_key(spreadsheet_id) #abrir arquivo


mais_faladas = spreadsheet.worksheet('mais_faladas')

conta_palavras(globo_sheet, mais_faladas)

conta_palavras(jp_sheet, mais_faladas)

conta_palavras(uol_sheet, mais_faladas)
