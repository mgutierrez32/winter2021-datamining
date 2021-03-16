"""
################## THIS IS A WORK IN PROGRESS ##################
################## DOES NOT WORK WITH CURRENT ##################
##################     MONGODB JSON EXPORT    ##################
This is the file we ran to compile our database of articles from
FOX, CNN, NPR, and AP. The program uses RSS feeds for the 4 news
sites and checks them every 10 minutes to see if any new articles
have been published. The program was originally running almost
nonstop for 7 weeks (from 1/25/21 to 3/15/21).
"""

import time
import json
import feedparser
import newspaper
import platform

if platform.system() == "Windows":
    path = 'ArticleDatabaseExport\articles.json'
else:
    path = 'ArticleDatabaseExport/articles.json'


def get_and_upload(url, site, article_list):
    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()
        article.nlp()
        article_list.append({"site": site, "url": article.url, "title": article.title,
                             "text": article.text, "keywords": article.keywords,
                             "summary": article.summary, "meta-descr": article.meta_description})
    except newspaper.ArticleException:
        print("Error 404 for Article")


if __name__ == '__main__':
    while True:
        articles = json.load(open(path, 'r', encoding='utf-8'))

        # FOX
        links = [x["url"] for x in articles if x["site"] == "FOX"]
        d = feedparser.parse('http://feeds.foxnews.com/foxnews/latest')
        for i in range(len(d.entries)):
            if d.entries[i].link not in links:
                links.append(d.entries[i].link)
                get_and_upload(d.entries[i].link, 'FOX', articles)
        print("FOX: ", len(links))

        # CNN
        links = [x["url"] for x in articles if x["site"] == "CNN"]
        d = feedparser.parse('http://rss.cnn.com/rss/cnn_latest.rss')
        for i in range(len(d.entries)):
            if d.entries[i].id not in links:
                links.append(d.entries[i].id)
                get_and_upload(d.entries[i].id, 'CNN', articles)
        d = feedparser.parse('http://rss.cnn.com/rss/cnn_topstories.rss')
        for i in range(len(d.entries)):
            if d.entries[i].id not in links:
                links.append(d.entries[i].id)
                get_and_upload(d.entries[i].id, 'CNN', articles)
        print("CNN: ", len(links))

        # NPR
        links = [x["url"] for x in articles if x["site"] == "NPR"]
        d = feedparser.parse('http://www.npr.org/rss/rss.php?id=1001')
        for i in range(len(d.entries)):
            if d.entries[i].link not in links:
                links.append(d.entries[i].link)
                get_and_upload(d.entries[i].link, 'NPR', articles)
        print("NPR: ", len(links))

        # AP
        links = [x["url"] for x in articles if x["site"] == "AP"]
        d = feedparser.parse('https://rsshub.app/apnews/topics/apf-topnews')
        for i in range(len(d.entries)):
            if d.entries[i].link not in links:
                links.append(d.entries[i].link)
                get_and_upload(d.entries[i].link, 'AP', articles)
        print(" AP: ", len(links), "\n")

        with open(path, "w") as outfile:
            json.dump(articles, outfile, indent=4)

        time.sleep(600)

