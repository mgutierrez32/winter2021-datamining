from nltk import classify
from nltk import NaiveBayesClassifier
import cleaning_article 


def get_dictionary(cleaned_tokens_list):
    """
    Turns list of tokens into a dictionary with True.
    :param cleaned_tokens_list: List of lists of cleaned tokenized articles.
    :return:
    """
    for tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tokens)

left_tokens_for_model = list(get_dictionary(left_cleaned_tokens_list))
right_tokens_for_model = list(get_dictionary(right_cleaned_tokens_list))