import base64
import gspread
import json
import pandas as pd
import pytz
import os
import requests
import re
import time
from datetime import datetime

from contagem_candidatos import contagem_candidatos
from contagem_palavras import conta_palavras

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) # autenticação
spreadsheet = service_account.open_by_key(spreadsheet_id) #abrir arquivo

globo_sheet = spreadsheet.worksheet('globo') 
uol_sheet = spreadsheet.worksheet('uol') 
jp_sheet = spreadsheet.worksheet('jovem_pan') 
folha_sheet = spreadsheet.worksheet('folha') 
oglobo_sheet = spreadsheet.worksheet('oglobo') 


# Mais faladas
contagem_candidatos = spreadsheet.worksheet('contagem_candidato')
contagem_candidatos(globo_sheet, contagem_candidatos)

contagem_candidatos(uol_sheet, contagem_candidatos)

contagem_candidatos(jp_sheet, contagem_candidatos)

contagem_candidatos(folha_sheet, contagem_candidatos)

contagem_candidatos(oglobo_sheet, contagem_candidatos)
