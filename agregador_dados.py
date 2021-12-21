#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import glob


# In[2]:


arquivos_globo = []
for arquivo in glob.glob('C:\\Users\\victo\\OneDrive\\Documentos\\Master\\analise_jornais\\globo*csv'):
    arquivos_globo.append(arquivo)

tabelas_globo = []
for arquivo in arquivos_globo:
    tabelas_globo.append(pd.read_csv(arquivo, index_col=0))

arq_fim_globo = pd.concat(tabelas_globo).reset_index()
arq_fim_globo = arq_fim_globo.rename(columns={'0': 'data', '1': 'editoria', '2': 'posicao', '3': 'titulo', '4': 'link'})
arq_fim_globo


# In[3]:


arquivos_uol = []
for arquivo in glob.glob('C:\\Users\\victo\\OneDrive\\Documentos\\Master\\analise_jornais\\uol*csv'):
    arquivos_uol.append(arquivo)

tabelas_uol = []
for arquivo in arquivos_uol:
    tabelas_uol.append(pd.read_csv(arquivo, index_col=0))

arq_fim_uol = pd.concat(tabelas_uol).reset_index()
arq_fim_uol = arq_fim_uol.rename(columns={'0': 'data', '1': 'classe', '2': 'titulo', '3': 'link'})
arq_fim_uol


# In[ ]:




