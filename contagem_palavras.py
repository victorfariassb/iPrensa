import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist

def conta_palavras(base, contagem):
    if base == 'globo_sheet':
        linha = 2
    elif base == 'uol_sheet':
        linha = 3
    elif base == 'jp_sheet':
        linha == 4
    coluna = 1
    
    dataframe = pd.DataFrame(base.get_all_records()) 
    
    nltk.download('punkt') 
    
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
    
    fdist = FreqDist(filtered_sent2).most_common(10)
    contagem.update_cell(linha, coluna, fdist[0][0])
    contagem.update_cell(linha, coluna + 1, fdist[0][1])
    contagem.update_cell(linha, coluna + 2, fdist[1][0])
    contagem.update_cell(linha, coluna + 3, fdist[1][1])
    contagem.update_cell(linha, coluna + 4, fdist[2][0])
    contagem.update_cell(linha, coluna + 5, fdist[2][1])
    contagem.update_cell(linha, coluna + 6, fdist[3][0])
    contagem.update_cell(linha, coluna + 7, fdist[3][1])
    contagem.update_cell(linha, coluna + 8, fdist[4][0])
    contagem.update_cell(linha, coluna + 9, fdist[4][1])
    contagem.update_cell(linha, coluna + 10, fdist[5][0])
    contagem.update_cell(linha, coluna + 11, fdist[5][1])
    contagem.update_cell(linha, coluna + 12, fdist[6][0])
    contagem.update_cell(linha, coluna + 13, fdist[6][1])
    contagem.update_cell(linha, coluna + 14, fdist[7][0])
    contagem.update_cell(linha, coluna + 15, fdist[7][1])
    contagem.update_cell(linha, coluna + 16, fdist[8][0])
    contagem.update_cell(linha, coluna + 17, fdist[8][1])
    contagem.update_cell(linha, coluna + 18, fdist[9][0])
    contagem.update_cell(linha, coluna + 19, fdist[9][1])
