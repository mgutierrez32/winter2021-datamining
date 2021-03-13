"""
File used to match articles.

Given an article URL, package will return the top 5 matched articles from our
database of CNN and FOX articles.
"""


def compile_articles(fox=True, cnn=True, text=False):
    """
    This function compiles articles from the json file
    export of our

    :return:
    """
    import json

    fox_articles = []
    cnn_articles = []
    for line in open('articles.json', 'r', encoding="utf8"):
        article = json.loads(line)
        if article['site'] == 'FOX':
            if text:
                fox_articles.append(article['text'])
            else:
                fox_articles.append(article)
        elif article['site'] == 'CNN':
            if text:
                cnn_articles.append(article['text'])
            else:
                cnn_articles.append(article)
    if fox and not cnn:
        return fox_articles
    elif not fox and cnn:
        return cnn_articles
    else:
        return cnn_articles, fox_articles


def compile_politics(fox=True, cnn=True, text=False):
    """
    This function compiles articles from the json file
    export of our

    :return:
    """
    import json

    fox_articles = []
    cnn_articles = []
    for line in open('politics.json', 'r', encoding="utf8"):
        article = json.loads(line)
        if article['site'] == 'FOX':
            if text:
                fox_articles.append(article['text'])
            else:
                fox_articles.append(article)
        elif article['site'] == 'CNN':
            if text:
                cnn_articles.append(article['text'])
            else:
                cnn_articles.append(article)
    if fox and not cnn:
        return fox_articles
    elif not fox and cnn:
        return cnn_articles
    else:
        return cnn_articles, fox_articles


left, right = compile_articles(text=True)
