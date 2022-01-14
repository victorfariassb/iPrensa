import gspread

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist

def conta_palavras(base, contagem):
    linha = 2
    coluna = 1
    
    nltk.download('punkt') 
    
    #String text pega todos os títulos do arquivo
    text = ''
    for index, row in base.iterrows():
        text = text + row['titulo'].lower() + ' ' 

    #Sentence tokenizer breaks text paragraph into sentences.
    tokenized_text = sent_tokenize(text)

    #Word tokenizer breaks text paragraph into words.
    tokenized_word = word_tokenize(text)
    
    nltk.download('stopwords')

    stop_words = set(stopwords.words("portuguese"))
    for x in ['seção','@','#',',', '!', ':', 'vídeo', 'quer', 'uol', 'vai', 'carros', 'pode', 'novo', 'afirma', '2021', 'confira', 'durante', '.', 'a', 'sobre', 'diz', 'após', 'veja', 'ser', 'faz', 'ex',
              'r', '1', '4', '9', '2', '3', '5', '6', '7', '8', 'anos', 'ano', '2022', 'dia', 'contra', 'virada', 'melhores', 'mil', '19', 'fotos', 'foto', 'fazer']:
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
    
    fdist = FreqDist(filtered_sent2)
    contagem.update_cell(linha, coluna, fdist[0])
    contagem.update_cell(linha, coluna + 1, fdist[1])
    contagem.update_cell(linha, coluna + 2, fdist[2])
    contagem.update_cell(linha, coluna + 3, fdist[3])
    contagem.update_cell(linha, coluna + 4, fdist[4])
    contagem.update_cell(linha, coluna + 5, fdist[5])
    contagem.update_cell(linha, coluna + 6, fdist[6])
    contagem.update_cell(linha, coluna + 7, fdist[7])
    contagem.update_cell(linha, coluna + 8, fdist[8])
    contagem.update_cell(linha, coluna + 9, fdist[9])
    linha += 1
