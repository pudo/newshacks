import os
import dataset
import hashlib
#from gensim import corpora, models, similarities


def get_engine():
    url = os.environ.get('DATABASE_URL', 'sqlite:///articles.sqlite3')
    return dataset.connect(url)

#DICTIONARIES = '.dicts'

#def article_path(url):
#    if not os.path.isdir(DICTIONARIES):
#        os.makedirs(DICTIONARIES)
#    fn = hashlib.sha1(url).hexdigest()
#    return os.path.join(DICTIONARIES, fn)

#def save_article_dict(url, tokens):
#    dic = corpora.Dictionary(tokens)
#    dic.save(article_path(url))
#    return dic

#def load_article_dict(url):
#    return corpora.Dictionary.load(article_path(url))
