#!/usr/bin/env python
# coding: utf-8

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


# Raspagem de dados
globo_sheet = spreadsheet.worksheet('globo') # escolhe aba

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
    num = 0
    
    now = datetime.now(pytz.timezone('Brazil/East'))
    dia = now.strftime("%d/%m/%Y %H:%M:%S")
    
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
        globo_sheet.append_row([f"materia {num}", dia, editoria, titulo, posicao, link])
    
    
coleta_globo()


uol_sheet = spreadsheet.worksheet('uol') # escolhe aba

def coleta_uol():
    num = 0
    time.sleep(5)
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
                        uol_sheet.append_row([f'materia {num}', dia, classe, link, titulo])

                        
coleta_uol()

jp_sheet = spreadsheet.worksheet('jovem_pan') 

def pega_link(link):
    action = link.attrs.get('href')
    if not action and link.parent:
        return pega_link(link.parent)
    else:
        return action

def coleta_jp():
    num = 0
    time.sleep(5)

    now = datetime.now(pytz.timezone('Brazil/East'))
    dia = now.strftime("%d/%m/%Y %H:%M:%S")

    resposta = requests.get("https://jovempan.com.br/")
    html = resposta.text
    soup = bs(html, 'html.parser')
    for manchete in soup.find_all('h2', class_='title'):
        editoria = manchete.parent.parent.find('h6', class_='category')
        if editoria:
            num += 1
            titulo = manchete.text
            tipo = 'manchete'
            link = pega_link(manchete)
            editoria = editoria.text
            jp_sheet.append_row([dia, editoria, titulo, tipo, link])

    for manchete_inferior in soup.find_all('h3', class_='title'):
        editoria = manchete_inferior.parent.parent.find('h6', class_='category')
        if editoria:
            time.sleep(2)
            num += 1
            titulo = manchete_inferior.text
            tipo = 'manchete_inferior'
            link = pega_link(manchete_inferior)
            editoria = editoria.text
            jp_sheet.append_row([dia, editoria, titulo, tipo, link])

    for dado in soup.find_all('p', class_='title'):
        titulo = dado.text.strip()
        if titulo:
            time.sleep(2)
            num += 1    
            editoria = dado.parent.find('h6', class_='category')
            if editoria is not None:
                editoria = editoria.text.strip()
            else:
                editoria = None
            tipo = 'noticias'
            link = pega_link(dado)
            if 'curso' not in str(link):
                jp_sheet.append_row([dia, editoria, titulo, tipo, link])
        
   
coleta_jp()


folha_sheet = spreadsheet.worksheet('folha') # escolhe aba

def coleta_folha():
  time.sleep(5)
  now = datetime.now(pytz.timezone('Brazil/East'))
  dia = now.strftime("%d/%m/%Y %H:%M:%S")

  browser.get("https://www.folha.uol.com.br/")
  last_height = browser.execute_script("return document.body.scrollHeight")

  while True:
      browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(20)
      new_height = browser.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

  source = browser.find_element_by_tag_name('html')
  html = source.get_attribute('innerHTML')
  soup = bs(html, 'html.parser')
  for texto in soup.find_all('h2'):
        link = texto.parent.get('href')
        if link:
            titulo = texto.text.strip()
            classe = texto.get('class')
            classe = str(classe)
            classe = re.sub("\['", '', classe)
            classe = re.sub("\']", '', classe)      
            if classe:
                time.sleep(2)
                folha_sheet.append_row([dia, titulo, classe, link])
  
  top5 = soup.find('ol', class_='c-most-read__list')
  for item in top5.find_all('a'):
    time.sleep(2)
    titulo = item.text.strip()
    link = item.get('href')
    titulo = re.sub(r"\n+\s+", ': ', titulo)
    classe = 'mais lidas'
    folha_sheet.append_row([dia, titulo, classe, link])

coleta_folha()

oglobo_sheet = spreadsheet.worksheet('oglobo') # escolhe aba

def coleta_oglobo():
  now = datetime.now(pytz.timezone('Brazil/East'))
  dia = now.strftime("%d/%m/%Y %H:%M:%S")
    
  browser.get("https://oglobo.globo.com/")
  last_height = browser.execute_script("return document.body.scrollHeight")

  while True:
      browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(40)
      new_height = browser.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
          break
      last_height = new_height

  source = browser.find_element_by_tag_name('html')
  html = source.get_attribute('innerHTML')
  soup = bs(html, 'html.parser')

  for texto in soup.find_all('h1'):
    item = texto.find("a", href=True)
    if item == None:
      next
    else:
      titulo = item.text.strip()
      classe = item.parent.get('class')
      classe = str(classe)
      classe = re.sub("\['", '', classe)
      classe = re.sub("\']", '', classe)
      if 'block-header--title' not in classe:
        time.sleep(2)
        link = item.get('href')
        oglobo_sheet.append_row([dia, titulo, classe, link])
        
coleta_oglobo()

# Contagem de candidatos
time.sleep(20)
contagem_candidato = spreadsheet.worksheet('contagem_candidato')
contagem_candidatos(globo_sheet, contagem_candidato)
contagem_candidatos(uol_sheet, contagem_candidato)
contagem_candidatos(jp_sheet, contagem_candidato)
contagem_candidatos(folha_sheet, contagem_candidato)
contagem_candidatos(oglobo_sheet, contagem_candidato)


# Mais faladas
time.sleep(20)
mais_faladas = spreadsheet.worksheet('mais_faladas')
conta_palavras(globo_sheet, mais_faladas)
conta_palavras(uol_sheet, mais_faladas)
conta_palavras(jp_sheet, mais_faladas)
conta_palavras(folha_sheet, mais_faladas)
conta_palavras(oglobo_sheet, mais_faladas)
