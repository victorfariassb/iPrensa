#!/usr/bin/env python
# coding: utf-8

# In[ ]:
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

# In[ ]:

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = os.environ["GOOGLE_CHROME_PATH"]
browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=ChromeDriverManager().install())

spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials) # autenticação
spreadsheet = service_account.open_by_key(spreadsheet_id) #abrir arquivo
worksheet = spreadsheet.worksheet('globo') # escolhe aba

# Função recursiva para coletar editoria de matérias
def pega_editoria(link):
    action = link.attrs.get('data-tracking-action')
    if  not action and link.parent:
        return pega_editoria(link.parent)
    else: return action
    
def pega_localizacao(link):
    action = link.attrs.get('data-tracking-category')
    if  not action and link.parent:
        return pega_localizacao(link.parent)
    else: return action
    

def coleta_globo():
    globo = {}
    num = 0
    
    now = datetime.now(pytz.timezone('Brazil/East'))
    dia = now.strftime("%d/%m/%Y")
    hora = now.strftime("%H:%M:%S")
    
    browser.get("https://www.globo.com/")
    source = browser.find_element_by_tag_name('html')
    html = source.get_attribute('innerHTML')
    soup = bs(html, 'html.parser')
    for dado in soup.find_all('a', class_="post__link"):
        time.sleep(2)
        num += 1
        editoria = pega_editoria(dado)
        titulo = dado.get('title')
        titulo = re.sub(r"\n+", '', titulo)
        posicao = pega_localizacao(dado)
        link = dado.get('href')
        worksheet.append_row([f"materia {num}", dia, hora, editoria, titulo, posicao, link])
        globo[f'materia {num}'] = [dia, hora, editoria, posicao, titulo, link]

    df_globo = pd.DataFrame({key: pd.Series(value) for key, value in globo.items()}).T
    return df_globo

coleta_globo()

worksheet = spreadsheet.worksheet('uol') # escolhe aba

def coleta_uol():
    uol = {}
    num = 0
    classes_drop = ['headerDesktop__logo__hyperlink', 'linkExternal', 'followVideo__link', 'cardVideo__content__titleBrand__link',
                    'headerCard__link', 'headerSection__link', 'headlineAd__link']
    
    now = datetime.now(pytz.timezone('Brazil/East'))
    dia = now.strftime("%d/%m/%Y")
    hora = now.strftime("%H:%M:%S")    
    
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
                        worksheet.append_row([f'materia {num}', dia, hora classe, link, titulo])
                        uol[f'materia {num}'] = [dia, hora, classe, titulo, link]
    df_uol = pd.DataFrame({key: pd.Series(value) for key, value in uol.items()}).T
    return df_uol

coleta_uol()
