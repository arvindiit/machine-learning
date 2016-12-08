import pickle

import numpy
from domain.sentimentitem import SenetimentNewsItemCollection
from gensim.models import Doc2Vec
from sklearn.linear_model import SGDClassifier
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing.data import normalize

doc2vecModel = Doc2Vec().load("model/doc2vec_all_shuf_imdb_review_1.sv")

testNewsItems = SenetimentNewsItemCollection("data/test-json.txt")

trainNewsItems = SenetimentNewsItemCollection("data/train-json.txt")


trainingData = numpy.asarray([doc2vecModel.infer_vector(newsItem.getWords()) for newsItem in trainNewsItems.get_news_items()])
trainingLabels = [newsItem.getSentiment() for newsItem in trainNewsItems.get_news_items()]

multilabelbinarizer = MultiLabelBinarizer()
multilabelbinarizer.fit([['positive', 'negative']])

testData = numpy.asarray([doc2vecModel.infer_vector(newsItem.getWords()) for newsItem in testNewsItems.get_news_items()])
testLabels = [newsItem.getSentiment() for newsItem in testNewsItems.get_news_items()]


trainingData = normalize(trainingData)
testData = normalize(testData)

lr = SGDClassifier(loss='log', penalty='l1')
lr.fit(trainingData, trainingLabels)
lr.predict(testData)
with open('model/sentiment-classifier', 'wb') as fid:
    pickle.dump(lr, fid)

print('Test Accuracy: %.2f' % lr.score(testData, testLabels))