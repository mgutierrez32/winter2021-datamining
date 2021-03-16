# winter2021-datamining 

### Authors: Miguel Gutierrez, [Yue Shen](https://github.com/yzsshen) and [Ana Ysasi](https://github.com/anapysasi)

Final project for Dr. Anil Chaturvedi's Data Mining Principles course at the University of Chicago's Master of Science in Analytics.

---

### Description:

By using the Naive Bayes Classifier, this repository rates articles depending on the political inclination, giving a porcentage of `rigth` and `left` leaning and a `extremity score` (how extreme the item leans to one side or the other).

The actual accuracy of the model is `0.8302658486707567`. It also provides a list of the `Most Informative Features`.

![Demo of the code](https://github.com/mgutierrez32/winter2021-datamining/blob/main/Demo.gif)

---

### Instalation Guide

```python
pip3 install gitpython

import os
from git.repo.base import Repo
Repo.clone_from("https://github.com/mgutierrez32/winter2021-datamining", "folderToSave")
```

### Quickstart Guide

#### Folder: `ArticleDatabaseExport`

Json files of articles from CNN, fox, AP and NPR from Autumn quarter 2021. 

* `Articles.json` have all the articles.
* `politics.json` have only the political articles. This set was the one used to train the model.

#### File: `article_rss_webscraper.py`

#### File: `cleaning_article.py`

File used to clean the webscrapped articles. Takes care of removing the adds, tokenize the text and remove the most used words in the english language.

#### File: `matching_articles.py`

File used to match articles. Given an article URL, package will return the top 5 matched articles from our database of CNN and FOX articles.

#### File: `article_classifier.py`

File used to classify articles using a Naive Bayes Classifier.

Given an article URL, the package will classify the article as left-leaning or right-leaning and give the probability that the article is left or right, as well as giving a score as to how extreme the article leans towards one side or the other.

When run, this file also calls and implements the `matching_articles.py`file and returns headline of the closest CNN and FOX articles. 

### File: `use_case.py`

Example of a posible application of the article classifier. We have taken all the articles in our database (corresponding to all the articles published in Autumn quarter 2021) from NPR and AP and we have studied the percentage of left-leaning and rigth-leaning articles from each site.
