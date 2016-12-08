from collections import Counter

from domain.newsitem import NewsItemCollection

min_tag_count = 25

testNewsItems = NewsItemCollection("data/classification-test.txt")
trainNewsItems = NewsItemCollection("data/classification-train.txt")

c = Counter()
c.update([tag for newsItem in testNewsItems.get_news_items() for tag in newsItem.getTags()])
c.update([tag for newsItem in trainNewsItems.get_news_items() for tag in newsItem.getTags()])
common_tags = [item[0] for item in c.items() if item[1] > min_tag_count]
print(common_tags)