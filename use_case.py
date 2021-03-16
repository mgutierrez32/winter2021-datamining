"""
File classifies articles from NPR and AP as left or right leaning
based on Naive Based

"""
from nltk import NaiveBayesClassifier
import newspaper
import cleaning_article
import matching_articles
from sklearn.model_selection import train_test_split
from multiprocessing import Pool
from article_classifier import get_dictionary


def compile_centrist_articles():
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

    ap_articles = []
    npr_articles = []
    for line in open(path, 'r', encoding='utf-8'):
        article = json.loads(line)
        if article['site'] == 'AP':
            ap_articles.append(article['url'])
        elif article['site'] == 'NPR':
            npr_articles.append(article['url'])
    return npr_articles, ap_articles


if __name__ == '__main__':
    # Compiling articles for dataset
    left_articles_text, right_articles_text = matching_articles.compile_politics(text=True)

    with Pool(processes=4) as pool:
        left_cleaned_tokens_list = pool.map(cleaning_article.run, left_articles_text)
        right_cleaned_tokens_list = pool.map(cleaning_article.run, right_articles_text)

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

    npr_articles_text, ap_articles_text = compile_centrist_articles()

    sites = ['NPR', 'AP']
    i = -1
    for site in [npr_articles_text, ap_articles_text]:
        i += 1
        print('data for: left', sites[i])
        total_left_prob = list()
        total_right_prob = list()
        total_ex_score = list()
        for url in site:
            try:
                # Webscrapes article text from a url
                article = newspaper.Article(url.strip())
                article.download()
                article.parse()

                custom_tokens = cleaning_article.run(article.text)

                dist = classifier.prob_classify(dict([token, True] for token in custom_tokens))
                list(dist.samples())

                left_prob = round(dist.prob('Left'), 4)
                right_prob = round(dist.prob('Right'), 4)
                total_left_prob.append(left_prob)
                total_right_prob.append(right_prob)

                ex_score = round(max(left_prob, right_prob) - min(left_prob, right_prob), 4)
                total_ex_score.append(ex_score)
            except AttributeError:
                print('\nSorry, unable to parse text from News Site :( ')

        NPR_total_left_prob = sum(total_left_prob)/len(total_left_prob)
        NPR_total_right_prob = sum(total_right_prob)/len(total_right_prob)
        NPR_total_ex_score_left = sum(total_ex_score)/len(total_ex_score)
        print('Total left probability:', NPR_total_left_prob)
        print('Total right probability:', NPR_total_right_prob)
        print('Total ex_score probability:', NPR_total_ex_score_left)
