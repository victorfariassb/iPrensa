import time
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist

def conta_palavras(base, contagem):
    dataframe = pd.DataFrame(base.get_all_records()) 
    dataframe = dataframe.drop_duplicates(subset='link', keep='first')
    chave = dataframe.columns[3]
    
    if chave == 'classe_globo':
        coluna = 1
    elif chave == "classe_uol":
        coluna = 3
    elif chave == "classe_jp":
        coluna = 5
    elif chave == 'classe_folha':
        coluna = 7
    elif chave == "classe_estadao":
        coluna = 9
    elif chave == "classe_cnn":
        coluna = 11

    else:
        coluna = 15
    linha = 2
    
    nltk.download('punkt') 
    
    # Contagem de mesmo tema
    dataframe['titulo'] = dataframe['titulo'].str.replace('BBB22', 'bbb')
    
    #String text pega todos os títulos do arquivo
    text = ''
    for index, row in dataframe.iterrows():
        text = text + row['titulo'].lower() + ' ' 

    #Sentence tokenizer breaks text paragraph into sentences.
    tokenized_text = sent_tokenize(text)

    #Word tokenizer breaks text paragraph into words.
    tokenized_word = word_tokenize(text)
    
    nltk.download('stopwords')

    stop_words = set(stopwords.words("portuguese"))
    for x in ['seção','@','#',',', '!', ':', 'vídeo', 'quer', 'uol', 'vai', 'carros', 'pode', 'novo', 'afirma', '2021', 'confira', 'durante', '.', 'a', 'sobre', 'diz', 'após', 'veja', 'ser', 'faz', 'ex', 'maior', '22',
              'r', '1', '4', '9', '2', '3', '5', '6', '7', '8', 'anos', 'ano', '2022', 'dia', 'contra', 'virada', 'melhores', 'mil', '19', 'fotos', 'foto', 'fazer', 'pede', 'momento', 'mostra', 'pede', 'momento', '0',
             'conheça', 'deve', 'hoje', 'entenda', 'blog', 'siga', 'casa', 'nova', 'ter']:
        stop_words.add(x)

    tokenized_sent = tokenized_word
    filtered_sent = []
    for w in tokenized_sent:
        if w not in stop_words:
            filtered_sent.append(w)

    tokenizer = RegexpTokenizer(r'\w+')
    filtered_sent = tokenizer.tokenize(' '.join(filtered_sent))
    filtered_sent2 = []
    for w in filtered_sent:
        if w not in stop_words:
            filtered_sent2.append(w)
    
    fdist = FreqDist(filtered_sent2).most_common(10)
    time.sleep(15)
    contagem.update_cell(linha, coluna, fdist[0][0])
    contagem.update_cell(linha, coluna + 1, fdist[0][1])
    contagem.update_cell(linha + 1, coluna, fdist[1][0])
    contagem.update_cell(linha + 1, coluna + 1, fdist[1][1])
    contagem.update_cell(linha + 2, coluna, fdist[2][0])
    contagem.update_cell(linha + 2, coluna + 1, fdist[2][1])
    contagem.update_cell(linha + 3, coluna, fdist[3][0])
    contagem.update_cell(linha + 3, coluna + 1, fdist[3][1])
    contagem.update_cell(linha + 4, coluna, fdist[4][0])
    contagem.update_cell(linha + 4, coluna + 1, fdist[4][1])
    contagem.update_cell(linha + 5, coluna, fdist[5][0])
    contagem.update_cell(linha + 5, coluna + 1, fdist[5][1])
    contagem.update_cell(linha + 6, coluna, fdist[6][0])
    contagem.update_cell(linha + 6, coluna + 1, fdist[6][1])
    contagem.update_cell(linha + 7, coluna, fdist[7][0])
    contagem.update_cell(linha + 7, coluna + 1, fdist[7][1])
    contagem.update_cell(linha + 8, coluna, fdist[8][0])
    contagem.update_cell(linha + 8, coluna + 1, fdist[8][1])
    contagem.update_cell(linha + 9, coluna, fdist[9][0])
    contagem.update_cell(linha + 9, coluna + 1, fdist[9][1])
