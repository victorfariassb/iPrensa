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
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = os.environ["GOOGLE_CHROME_PATH"]
browser = webdriver.Chrome(options=options)


# Raspagem de dados
# Função recursiva para coletar editoria de matérias
def pega_editoria_globo(link):
    action = link.attrs.get('data-tracking-action')
    if  not action and link.parent:
        return pega_editoria_globo(link.parent)
    else: return action
    
def pega_localizacao(link):
    action = link.attrs.get('data-tracking-category')
    if  not action and link.parent:
        return pega_localizacao(link.parent)
    else: return action

def pega_link(link):
    action = link.attrs.get('href')
    if not action and link.parent:
        return pega_link(link.parent)
    else:
        return action
    

def coleta_globo(planilha):
    num = 0
    
    now = datetime.now(pytz.timezone('Brazil/East'))
    dia = now.strftime("%d/%m/%Y %H:%M:%S")
    
    browser.get("https://www.globo.com/")
    source = browser.find_element(By.TAG_NAME, 'html')
    html = source.get_attribute('innerHTML')
    soup = bs(html, 'html.parser')
    for dado in soup.find_all('a', class_="post__link"):
        time.sleep(2)
        num += 1
        editoria = pega_editoria_globo(dado)
        titulo = dado.get('title')
        if titulo:
            titulo = re.sub(r"\n+", '', titulo)
            posicao = pega_localizacao(dado)
            link = dado.get('href')
            planilha.append_row([num, dia, titulo, posicao, link, editoria])
        else:
            next


def coleta_uol(planilha):
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
                        planilha.append_row([num, dia, titulo, classe, link])

                       

def coleta_jp(planilha):
    num = 0

    now = datetime.now(pytz.timezone('Brazil/East'))
    dia = now.strftime("%d/%m/%Y %H:%M:%S")

    resposta = requests.get("https://jovempan.com.br/")
    html = resposta.text
    soup = bs(html, 'html.parser')
    manchetao = soup.find(id='jp-featured-posts-35')
    if manchetao:
      for materia in manchetao.find_all('a'):
        if materia.text:
          time.sleep(2)
          num +=1
          titulo = materia.text
          link = pega_link(materia)
          editoria = 'manchetao'
          planilha.append_row([num, dia, editoria, titulo, link])
    for manchete in soup.find_all(class_='title'):
        editoria = manchete.parent.parent.find('h6', class_='category')
        titulo = manchete.text.strip()
        if editoria:
            if titulo:
                time.sleep(2)
                num += 1            
                link = pega_link(manchete)
                editoria = editoria.text.strip()
                planilha.append_row([num, dia, editoria, titulo, link])

        
  

def coleta_folha(planilha):
  num = 0

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

  source = browser.find_element(By.TAG_NAME, 'html')
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
                num += 1
                planilha.append_row([num, dia, titulo, classe, link])
  
  top5 = soup.find('ol', class_='c-most-read__list')
  for item in top5.find_all('a'):
    time.sleep(1)
    titulo = item.text.strip()
    link = item.get('href')
    titulo = re.sub(r"\n+\s+", ': ', titulo)
    classe = 'mais lidas'
    num += 1
    planilha.append_row([num, dia, titulo, classe, link])


def coleta_oglobo(planilha):
    num = 0
    now = datetime.now(pytz.timezone('Brazil/East'))
    dia = now.strftime("%d/%m/%Y %H:%M:%S")

    browser.get("https://oglobo.globo.com/")
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    source = browser.find_element(By.TAG_NAME, 'html')
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
            num += 1
            planilha.append_row([num, dia, titulo, classe, link])

        
def coleta_estadao(planilha):
  num = 0
    
  now = datetime.now(pytz.timezone('Brazil/East'))
  dia = now.strftime("%d/%m/%Y %H:%M:%S")

  driver.get("https://www.estadao.com.br/")

  source = driver.find_element(By.TAG_NAME, 'html')
  html = source.get_attribute('innerHTML')
  soup = bs(html, 'html.parser')
  for manchete in soup.find_all('h2', class_='headline'):
    titulo = manchete.text
    link = manchete.parent.get('href')
    classe = link.split('/')[3]
    planilha.append_row([num, dia, titulo, classe, link])
for bullet in soup.find_all('div', class_='bullets'):
    data = bullet.find('a')
    titulo = data.text
    link = data.get('href')
    classe = link.split('/')[3]
    planilha.append_row([num, dia, titulo, classe, link])

def pega_editoria_cnn(editoria):
    action = editoria.find(class_='home__category')
    business = editoria.find(class_='home__business')
    home = editoria.find(class_='home__list')
    if not action and editoria.parent:
      if business:
        return business.text
      elif home:
        return 'sem editoria'
      return pega_editoria_cnn(editoria.parent)
    else: 
        return action.text

def coleta_cnn(planilha):
  num = 0
  
  now = datetime.now(pytz.timezone('Brazil/East'))
  dia = now.strftime("%d/%m/%Y %H:%M:%S")

  browser.get("https://www.cnnbrasil.com.br/")


  source = browser.find_element(By.TAG_NAME, 'html')
  html = source.get_attribute('innerHTML')

  soup = bs(html, 'html.parser')
  for materia in soup.find_all(class_='home__title'):
    editoria = pega_editoria_cnn(materia)
    if editoria != 'Branded content':
      time.sleep(2)
      num += 1
      link = pega_link(materia)
      titulo = materia.text
      planilha.append_row([num, dia, titulo, editoria, link])
  

 
