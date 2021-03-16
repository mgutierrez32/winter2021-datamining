"""
File classifies articles from NPR and AP as left or right leaning
based on Naive Based

"""
from nltk import classify
from nltk import NaiveBayesClassifier
import newspaper
import cleaning_article
import matching_articles
import requests
from sklearn.model_selection import train_test_split
from multiprocessing import Pool
from article_classifier import get_dictionary


def compile_centrist_articles(ap=True, npr=True, text=False):
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

    ap_articles = []
    npr_articles = []
    for line in open(path, 'r', encoding = 'utf-8'):
        article = json.loads(line)
        if article['site'] == 'AP':
            if text:
                ap_articles.append(article['text'])
            else:
                ap_articles.append(article)
        elif article['site'] == 'NPR':
            if text:
                npr_articles.append(article['text'])
            else:
                npr_articles.append(article)
    if ap and not npr:
        return ap_articles
    elif not ap and npr:
        return npr_articles
    else:
        return npr_articles, ap_articles


if __name__ == '__main__':
    # Compiling articles for dataset
    left_articles_text, right_articles_text = matching_articles.compile_politics(text=True)

    with Pool(processes=4) as pool:
        left_cleaned_tokens_list = pool.map(cleaning_article.run, left_articles_text)
        right_cleaned_tokens_list = pool.map(cleaning_article.run, right_articles_text)

    # left_cleaned_tokens_list = cleaning_article.run(left_articles_text)
    # right_cleaned_tokens_list = cleaning_article.run(right_articles_text)

    left_tokens_for_model = list(get_dictionary(left_cleaned_tokens_list))
    right_tokens_for_model = list(get_dictionary(right_cleaned_tokens_list))

    # Tagging with Left and Right
    left_dataset = [(left_dict, "Left")
                    for left_dict in left_tokens_for_model]

    right_dataset = [(right_dict, "Right")
                     for right_dict in right_tokens_for_model]

    dataset = left_dataset + right_dataset

    # Making train and test dataset split, 70/30
    Train, Test = train_test_split(dataset, random_state=6741, test_size=0.3)

    # Build classifier
    classifier = NaiveBayesClassifier.train(Train)

    # Test Validation
    print("Accuracy is:", classify.accuracy(classifier, Test))

    print(classifier.show_most_informative_features(20))

    npr_articles_text, ap_articles_text = compile_centrist_articles(text=True)