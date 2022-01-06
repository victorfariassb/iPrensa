import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk import FreqDist

def conta_palavras(arquivo):
    #String text pega todos os títulos do arquivo
    text = ''
    for index, row in arquivo.iterrows():
        text = text + row['titulo'].lower() + ' '
    
    nltk.download('punkt')  

    #Sentence tokenizer breaks text paragraph into sentences.
    tokenized_text = sent_tokenize(text)

    #Word tokenizer breaks text paragraph into words.
    tokenized_word = word_tokenize(text)
    
    nltk.download('stopwords')

    stop_words = set(stopwords.words("portuguese"))
    for x in ['seção','@','#',',', '!', ':', 'vídeo', 'quer', 'uol', 'vai', 'pode', 'novo', 'afirma', '2021', 'confira', 'durante', '.', 'a', 'sobre', 'diz', 'após', 'veja', 'ser', 'faz', 'ex',
              'r', '1', '4', '9', '2', '3', '5', '6', '7', '8', 'anos', 'ano', '2022', 'dia']:
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
    return fdist.most_common(5)
