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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('--no-sandbox')
options.binary_location = os.environ["GOOGLE_CHROME_PATH"]
browser = webdriver.Chrome(service=Service, options=options, executable_path=ChromeDriverManager().install())

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) 
spreadsheet = service_account.open_by_key(spreadsheet_id) 

uol_sheet = spreadsheet.worksheet('uol') 

num = 0
classes_drop = ['headerDesktop__logo__hyperlink', 'linkExternal', 'followVideo__link', 'cardVideo__content__titleBrand__link',
                'headerCard__link', 'headerSection__link', 'headlineAd__link']

now = datetime.now(pytz.timezone('Brazil/East'))
dia = now.strftime("%d/%m/%Y %H:%M:%S")

resposta = requests.get("https://www.uol.com.br/")
html = resposta.text
soup = bs(html, 'html.parser')
for texto in soup.find_all('a'):
    next
    if 'class="hyperlink ' in str(texto): # gambiarra
        if 'class="hyperlink showcase' not in str(texto): # gambiarra
            if 'class="hyperlink blackBar' not in str(texto): # gambiarra
                next
                time.sleep(2) 
                classe = texto.get('class')[1]
                if classe in classes_drop:
                    next
                else:
                    num += 1
                    link = texto.get('href')
                    tit = texto.text
                    tit = tit.strip()
                    tit = re.sub(r"\n+\s+", ': ', tit)
                    titulo = tit
                    uol_sheet.append_row([num, dia, classe, link, titulo])
