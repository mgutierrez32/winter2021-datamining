# winter2021-datamining 

### Authors: Miguel Gutierrez, Yue Shen and Ana Ysasi

Final project for Dr. Anil Chaturvedi's class of Data Mining at the Univeristy of Chicago.

---

### Description:

By using the Naive Bayes Classifier, this repository rates articles depending on the political inclination, giving a porcentage of `rigth` and `left` leaning and a `extremity score` (how extreme the item leans to one side or the other).

The actual accuracy of the model is `0.8302658486707567`. It also provides a list of the `Most Informative Features`.
 
```diff
- Here I would like to add a .git of the usage of the code.
```

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

#### File: `cleaning_article.py`

File used to clean the webscrapped articles. Takes care of removing the adds, tokenize the text and remove the most used words in the english language.

#### File: `matching_articles.py`

File used to match articles. Given an article URL, package will return the top 5 matched articles from our database of CNN and FOX articles.

#### File: `article_classifier.py`

File used to classify articles using a Naive Bayes Classifier.

Given an article URL, the package will classify the article as left-leaning or right-leaning and give the probability that the article is left or right, as well as giving a score as to how extreme the article leans towards one side or the other.
