import spacy
import pt_core_news_sm
from collections import Counter, OrderedDict

nlp = pt_core_news_sm.load()

def conta_entidade(df):
  df = pd.DataFrame(df.get_all_records())
  df = df['titulo']
  text = ' '.join(df.col_values(1))

  doc = nlp(text)

  labels = [x.text for x in doc.ents]
  dicionario = Counter(labels)

  palavras = [palavra for palavra, contagem in dicionátio.most_common(10)]
  entidades.append_row([str(site), palavras])
 
