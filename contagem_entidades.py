import gspread
import base64
import os
import json
import pandas as pd
import spacy
import pt_core_news_sm
from collections import Counter, OrderedDict


spreadsheet_id = os.environ['GOOGLE_SHEET_ID']
conteudo_codificado =  os.environ['GOOGLE_SHEETS_CREDENTIALS']
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)

service_account = gspread.service_account_from_dict(credentials)
spreadsheet = service_account.open_by_key(spreadsheet_id) 

uol = spreadsheet.worksheet('uol')
globo = spreadsheet.worksheet('globo')
jp = spreadsheet.worksheet('jovem_pan')
entidades = spreadsheet.worksheet('entidades')

nlp = pt_core_news_sm.load()
nlp.max_length = 2000000

def conta_entidade(df):
  df = pd.DataFrame(site.get_all_records())   
  text = ''
  for index, row in df.iterrows():
    text = text + row['titulo'] + ' '

    doc = nlp(text)

  palavras = {}

  labels = [x.text for x in doc.ents]
  dicionario = Counter(labels)

  palavras = OrderedDict(sorted(dicionario.items(), key = lambda kv : kv[1], reverse=True))
  palavras = palavras.items()
  palavras = list(palavras)[:10]
  entidades.append_row([str(site), palavras])
  
  conta_entidade(uol)
  conta_entidade(globo)
  conta_entidade(jp)
