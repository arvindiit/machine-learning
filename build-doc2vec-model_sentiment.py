from gensim.models import Doc2Vec
import configparser
from domain.sentimentitem import SenetimentNewsItemCollection

configParser = configparser.ConfigParser()
configParser.read('config/config.ini', encoding="UTF-8")
config=configParser['DEFAULT']

newsItems = SenetimentNewsItemCollection('data/doc2vec-corpus-shuffled.txt')

model = Doc2Vec(workers=8, size=int(config['doc2vec_dimensions']), iter=10)
model.build_vocab(newsItems)
model.train(newsItems)

model.save("model/doc2vec_all_shuf_imdb_review_1.sv")