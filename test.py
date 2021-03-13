"""
File used to classify articles using a Naive Bayes Classifier.

Given an article URL, package will classify the article as
left-leaning or right-leaning and give the probability that
the article is left or right, as well as giving a score as
to how extreme the article leans towards one side or the other.
"""
import nltk
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
from nltk import classify
from nltk import NaiveBayesClassifier
import newspaper
import cleaning_article
import matching_articles
import requests
from sklearn.model_selection import train_test_split

def get_dictionary(cleaned_tokens_list):
    """
    Turns list of tokens into a dictionary with True.
    :param cleaned_tokens_list: List of lists of cleaned tokenized articles.
    :return: Returns a dictionary with key as the word/feature and value as "True"
    """
    for tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tokens)
        
# Compiling articles for dataset
# left_articles_text, right_articles_text = matching_articles.compile_articles(text=True)
# print('Text download successfully')
from pymongo import MongoClient
myclient = MongoClient("mongodb+srv://yzsshen:DataMining123@cluster0.csekt.mongodb.net/%3Cdbname%3E?retryWrites=true&w=majority")
db = myclient['DataMiningProject']
collection = db['Politics']
train_left = collection.find({'site': 'CNN'})
left_articles_text = []
for article in train_left:
    left_articles_text.append(article['text'])
print('Text download successfully (left)')
train_right = collection.find({'site': 'FOX'})
right_articles_text = []
for article in train_right:
    right_articles_text.append(article['text'])
print('Text download successfully (right)')

left_cleaned_tokens_list = cleaning_article.run(left_articles_text)
right_cleaned_tokens_list = cleaning_article.run(right_articles_text)
print('Cleaned text')

left_tokens_for_model = list(get_dictionary(left_cleaned_tokens_list))
right_tokens_for_model = list(get_dictionary(right_cleaned_tokens_list))
print('get dictionary')

# Tagging with Left and Right
left_dataset = [(left_dict, "Left")
                for left_dict in left_tokens_for_model]

right_dataset = [(right_dict, "Right")
                 for right_dict in right_tokens_for_model]

dataset = left_dataset + right_dataset
print('dataset')

# Making train and test dataset split, 70/30
Train, Test = train_test_split(dataset, random_state=6741, test_size=0.3)

# Build classifier
classifier = NaiveBayesClassifier.train(Train)
print('classifier')

# Test Validation
print("Accuracy is:", classify.accuracy(classifier, Test))

print(classifier.show_most_informative_features(20))

# Pass in url of article to classify
url_test = input('Copy an Article url Here: ')

# Webscrapes article text from a url
html = requests.get(url_test).text
text = newspaper.fulltext(html)

custom_tokens = cleaning_article.run(text)
print('The article is predicted as: ', classifier.classify(dict([token, True] for token in custom_tokens)))

dist = classifier.prob_classify(dict([token, True] for token in custom_tokens))
list(dist.samples())

left_prob = round(dist.prob('Left'), 4)
right_prob = round(dist.prob('Right'), 4)
print('Probability of being a left-leaning article:', left_prob)
print('Probability of being a right-leaning article:', right_prob)

ex_score = round(max(left_prob, right_prob) - min(left_prob, right_prob), 4)
print('Extremity score: ', ex_score)
