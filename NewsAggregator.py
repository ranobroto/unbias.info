import feedparser
import json
from newspaper import Article
import nltk
import time
import boto3

rss_feed_links = ["http://rss.cnn.com/rss/cnn_topstories.rss", "http://feeds.foxnews.com/foxnews/latest"]
output = []

for news_site in rss_feed_links:
    rss_feed = feedparser.parse(news_site)
    article_list = {"news_site":rss_feed.feed.title, "articles":[]}
    
    for article in rss_feed.entries:
        url = article.id
        article_parsed = Article(url)

        time.sleep(1)
        article_parsed.download()
        article_parsed.parse()
        article_parsed.nlp()

        article_list["articles"].append({"title": article.title, "url": article.id, "authors": article_parsed.authors, "summary":article_parsed.summary.replace('\n', '')})
        
    output.append(article_list)
    
print(json.dumps(output, indent=4))

with open('data.json', 'w') as outfile:
    json.dump(output, outfile)

# s3 = boto3.resource('s3')
# obj = s3.Object('news-aggregator','data.json')
# obj.put(Body=json.dumps(output))
