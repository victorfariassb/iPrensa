#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pytz
import os
import requests
import re
import pandas as pd
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
    agora = now.strftime("%d/%m/%Y %H:%M:%S")
    
    browser.get("https://www.globo.com/")
    source = browser.find_element_by_tag_name('html')
    html = source.get_attribute('innerHTML')
    soup = bs(html, 'html.parser')
    for dado in soup.find_all('a', class_="post__link"):
        num += 1
        editoria = pega_editoria(dado)
        titulo = dado.get('title')
        titulo = re.sub(r"\n+", '', titulo)
        posicao = pega_localizacao(dado)
        link = dado.get('href')
        globo[f'materia {num}'] = [agora, editoria, posicao, titulo, link]

    df_globo = pd.DataFrame({key: pd.Series(value) for key, value in globo.items()}).T
    return df_globo


def coleta_uol():
    uol = {}
    num = 0
    
    now = datetime.now(pytz.timezone('Brazil/East'))
    agora = now.strftime("%d/%m/%Y %H:%M:%S")
    
    resposta = requests.get("https://www.uol.com.br/")
    html = resposta.text
    soup = bs(html, 'html.parser')
    for texto in soup.find_all('a'):
        next
        if 'class="hyperlink ' in str(texto): # gambiarra
            if 'class="hyperlink showcase' not in str(texto): # gambiarra
                if 'class="hyperlink blackBar' not in str(texto): # gambiarra
                    next
                    num += 1 
                    classe = texto.get('class')[1]
                    link = texto.get('href')
                    tit = texto.text
                    tit = tit.strip()
                    tit = re.sub(r"\n+\s+", ': ', tit)
                    titulo = tit
                    uol[f'materia {num}'] = [agora, classe, titulo, link]
    df_uol = pd.DataFrame({key: pd.Series(value) for key, value in uol.items()}).T
    return df_uol

