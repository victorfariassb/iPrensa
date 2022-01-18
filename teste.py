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

from contagem_palavras import conta_palavras

options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
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
mais_faladas = spreadsheet.worksheet('mais_faladas')


oglobo_sheet = spreadsheet.worksheet('oglobo') # escolhe aba

def coleta_oglobo():
  browser.get("https://oglobo.globo.com/")
  last_height = browser.execute_script("return document.body.scrollHeight")

  while True:
      browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(30)
      new_height = browser.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

  source = driver.find_element_by_tag_name('html')
  html = source.get_attribute('innerHTML')
  soup = bs(html, 'html.parser')

  for texto in soup.find_all('h1'):
    item = texto.find("a", href=True)
    if item == None:
      next
    else:
      titulo = item.text.strip()
      classe = item.parent.get('class')
      if 'block-header--title' not in classe:
        time.sleep(2)
        link = item.get('href')
        oglobo_sheet.append_row([[dia, titulo, classe, link]])
        
coleta_oglobo()
