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
    import platform

    if platform.system() == "Windows":
        path = 'ArticleDatabaseExport\politics.json'
    else:
        path = 'ArticleDatabaseExport/politics.json'

    fox_articles = []
    cnn_articles = []
    for line in open(path, 'r', encoding = 'utf-8'):
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
    import platform
    fox_articles = []
    cnn_articles = []
    if platform.system() == "Windows":
        path = 'ArticleDatabaseExport\politics.json'
    else:
        path = 'ArticleDatabaseExport/politics.json'
    for line in open(path, 'r', encoding='utf-8'):
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


def create_lsi(texts):
    return 1


def match_article(url, dictionary, corpus, lsi):
    from newspaper import Article
    from gensim import similarities
    article = Article(url)
    article.download()
    article.parse()

    vec_bow = dictionary.doc2bow(article.text.lower().split())
    vec_lsi = lsi[vec_bow]
    index = similarities.MatrixSimilarity(lsi[corpus])
    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    return sims[0:4]

