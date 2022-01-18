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
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from contagem_candidatos import contagem_candidatos
from contagem_palavras import conta_palavras

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = os.environ["GOOGLE_CHROME_PATH"]
browser = webdriver.Chrome(options=options, executable_path=ChromeDriverManager().install())

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) # autenticação
spreadsheet = service_account.open_by_key(spreadsheet_id) #abrir arquivo

globo_sheet = spreadsheet.worksheet('globo') # escolhe aba
uol_sheet = spreadsheet.worksheet('uol') # escolhe aba
jp_sheet = spreadsheet.worksheet('jovem_pan') 
folha_sheet = spreadsheet.worksheet('folha') 
oglobo_sheet = spreadsheet.worksheet('oglobo') # escolhe aba


# Mais faladas

mais_faladas = spreadsheet.worksheet('mais_faladas')

conta_palavras(globo_sheet, mais_faladas)

conta_palavras(uol_sheet, mais_faladas)

conta_palavras(jp_sheet, mais_faladas)

conta_palavras(folha_sheet, mais_faladas)

conta_palavras(oglobo_sheet, mais_faladas)
