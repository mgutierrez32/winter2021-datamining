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
        path = 'ArticleDatabaseExport\articles.json'
    else:
        path = 'ArticleDatabaseExport/articles.json'

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
    :param fox:
    :param cnn:
    :param text:
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
    """

    :param texts:
    :return:
    """
    import cleaning_article
    import gensim
    from multiprocessing import Pool, TimeoutError

    with Pool(processes=4) as pool:
        texts = pool.map(cleaning_article.run, texts)

    #texts = cleaning_article.run(texts)
    dictionary = gensim.corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    lsi = gensim.models.LsiModel(corpus, id2word=dictionary, num_topics=300)
    return dictionary, corpus, lsi


def match_article(text, dictionary, corpus, lsi):
    """

    :param text:
    :param dictionary:
    :param corpus:
    :param lsi:
    :return:
    """
    from gensim import similarities
    import cleaning_article

    vec_bow = dictionary.doc2bow(cleaning_article.run(text))
    vec_lsi = lsi[vec_bow]
    index = similarities.MatrixSimilarity(lsi[corpus])
    sims = index[vec_lsi]
    sims = sorted(enumerate(sims), key=lambda item: -item[1])
    return sims[0:5]

