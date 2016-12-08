import json

import gensim
from gensim.models.doc2vec import TaggedDocument


class SenetimentNewsItem(object):
    def __init__(self, jsonString):
        self.newsItem = json.loads(jsonString)

    def getWords(self):
        return gensim.utils.simple_preprocess(self.newsItem['content'])

    def getSentiment(self):
        return self.newsItem['sentiment']


class SenetimentNewsItemCollection(object):
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        counter = -1
        with open(self.file, encoding="UTF-8") as f:
            for line in f:
                newsItem = SenetimentNewsItem(line)
                counter += 1
                yield TaggedDocument(newsItem.getWords(), [counter])

    def get_news_items(self, tagFilter=[], limit=-1):
        counter = 0
        with open(self.file, encoding="UTF-8") as f:
            for line in f:
                # stop when limit is set and reached
                if limit > -1 and counter >= limit:
                    break;
                counter += 1

                newsItem = SenetimentNewsItem(line)
                yield newsItem