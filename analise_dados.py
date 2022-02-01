import base64
import gspread
import json
import os

from contagem_candidatos import contagem_candidatos
from contagem_palavras import conta_palavras

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) # autenticação
spreadsheet = service_account.open_by_key(spreadsheet_id) #abrir arquivo

# Abre as planilhas
globo_sheet = spreadsheet.worksheet('globo') 
uol_sheet = spreadsheet.worksheet('uol') 
jp_sheet = spreadsheet.worksheet('jovem_pan') 
folha_sheet = spreadsheet.worksheet('folha') 
oglobo_sheet = spreadsheet.worksheet('oglobo') 
estadao_sheet = spreadsheet.worksheet('estadao') 
contagem_candidato = spreadsheet.worksheet('contagem_candidato')


# Contagem de candidatos
contagem_candidatos(globo_sheet, contagem_candidato)
contagem_candidatos(uol_sheet, contagem_candidato)
contagem_candidatos(jp_sheet, contagem_candidato)
contagem_candidatos(folha_sheet, contagem_candidato)
contagem_candidatos(oglobo_sheet, contagem_candidato)
contagem_candidatos(estadao_sheet, contagem_candidato)


# Mais faladas
mais_faladas = spreadsheet.worksheet('mais_faladas')
conta_palavras(globo_sheet, mais_faladas)
conta_palavras(uol_sheet, mais_faladas)
conta_palavras(jp_sheet, mais_faladas)
conta_palavras(folha_sheet, mais_faladas)
conta_palavras(oglobo_sheet, mais_faladas)
conta_palavras(estadao_sheet, mais_faladas)
