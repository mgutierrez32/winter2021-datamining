import nltk
nltk.download('punkt')
nltk.download('wordnet') 
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
from nltk.corpus import wordnet as wn 
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer 
Lem = WordNetLemmatizer() 
from nltk.corpus import stopwords
from gensim.parsing.preprocessing import remove_stopwords
import re, string 

def cleaningSpecifics(phrase):
    phrase = re.sub(r"\n\nLoading...\n\nNote: This story was updated at \d+:\d+ \w.\w. \w+ \w+ \w+|[.] \d+", "", phrase)
    phrase = re.sub(r"and will be updated periodically, as new data are released.", "", phrase)
    phrase = re.sub(r"Loading...", "", phrase)
    phrase = re.sub(r"This story was originally published on \w+|[.] \d+, \d+", "", phrase)
    phrase = re.sub(r"\w+ contributed to this report", "", phrase)
    phrase = re.sub(r"\w+ \w+ contributed to this report", "", phrase)
    phrase = re.sub(r"\w+ \w+ \w+ contributed to this report", "", phrase) 
    phrase = re.sub(r"CLICK HERE FOR MORE SPORTS COVERAGE ON FOXNEWS.COM", "", phrase)
    phrase = re.sub(r"CLICK HERE TO GET THE FOX NEWS APP", "", phrase)
    phrase = re.sub(r"\n\n[A-Z\s\d\'\-\!,\@\#\$\%\^\&\*\(\)\[\+\=\]\{\}:;\.<>]{1,}\n\n", "", phrase)
    phrase = re.sub(r"ADVERTISEMENT", "", phrase)
    phrase = re.sub(r"Read More", "", phrase) 
    phrase = re.sub(r"^\(CNN\)", "", phrase) 
    phrase = re.sub(r'\bAL\b', 'Alabama', phrase)
    phrase = re.sub(r'\bAK\b','Alaska', phrase)
    phrase = re.sub(r'\bAZ\b', 'Arizona', phrase)
    phrase = re.sub(r'\bAR\b', 'Arkansas', phrase)
    phrase = re.sub(r'\bCA\b', 'California', phrase)
    phrase = re.sub(r'\bC\b', 'Colorado', phrase)
    phrase = re.sub(r'\bCT\b', 'Connecticut', phrase)
    phrase = re.sub(r'\bDE\b', 'Delaware', phrase)
    phrase = re.sub(r'\bFL\b', 'Florida', phrase)
    phrase = re.sub(r'\bGA\b', 'Georgia', phrase)
    phrase = re.sub(r'\bHI\b', 'Hawaii', phrase)
    phrase = re.sub(r'\bID\b', 'Idaho', phrase)
    phrase = re.sub(r'\bIL\b', 'Illinois', phrase)
    phrase = re.sub(r'\bIN\b', 'Indiana', phrase)
    phrase = re.sub(r'\bIA\b', 'Iowa', phrase)
    phrase = re.sub(r'\bKS\b', 'Kansas', phrase)
    phrase = re.sub(r'\bKY\b', 'Kentucky', phrase)
    phrase = re.sub(r'\bLA\b', 'Louisiana', phrase)
    phrase = re.sub(r'\bME\b', 'Maine', phrase)
    phrase = re.sub(r'\bMD\b', 'Maryland', phrase)
    phrase = re.sub(r'\bMA\b', 'Massachusetts', phrase)
    phrase = re.sub(r'\bMI\b', 'Michigan', phrase)
    phrase = re.sub(r'\bMN\b', 'Minnesota', phrase)
    phrase = re.sub(r'\bMS\b', 'Mississippi', phrase)
    phrase = re.sub(r'\bMO\b', 'Missouri', phrase)
    phrase = re.sub(r'\bMT\b', 'Montana', phrase)
    phrase = re.sub(r'\bNE\b', 'Nebraska', phrase)
    phrase = re.sub(r'\bNV\b', 'Nevada', phrase)
    phrase = re.sub(r'\bNH\b', 'New Hampshire', phrase)
    phrase = re.sub(r'\bNJ\b', 'New Jersey', phrase)
    phrase = re.sub(r'\bNM\b', 'New Mexico', phrase)
    phrase = re.sub(r'\bNY\b', 'New York', phrase)
    phrase = re.sub(r'\bNC\b', 'North Carolina', phrase)
    phrase = re.sub(r'\bND\b', 'North Dakota', phrase)
    phrase = re.sub(r'\bOH\b', 'Ohio', phrase)
    phrase = re.sub(r'\bOK\b', 'Oklahoma', phrase)
    phrase = re.sub(r'\bOR\b', 'Oregon', phrase)
    phrase = re.sub(r'\bPA\b', 'Pennsylvania', phrase)
    phrase = re.sub(r'\bRI\b', 'Rhode Island', phrase)
    phrase = re.sub(r'\bSC\b', 'South Carolina', phrase)
    phrase = re.sub(r'\bSD\b', 'South Dakota', phrase)
    phrase = re.sub(r'\bTN\b', 'Tennessee', phrase)
    phrase = re.sub(r'\bTX\b', 'Texas', phrase)
    phrase = re.sub(r'\bUT\b', 'Utah', phrase)
    phrase = re.sub(r'\bVT\b', 'Vermont', phrase)
    phrase = re.sub(r'\bVA\b', 'Virginia', phrase)
    phrase = re.sub(r'\bWA\b', 'Washington', phrase)
    phrase = re.sub(r'\bWV\b', 'West Virginia', phrase)
    phrase = re.sub(r'\bWI\b', 'Wisconsin', phrase)
    phrase = re.sub(r'\bWY\b', 'Wyoming', phrase)
    return phrase

def cleaning(phrase): 
    phrase = re.sub(r"won\'t", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)  
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase) 
    phrase = re.sub(r"\'s", "", phrase) 
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    phrase = re.sub(r"covid\-19", " covid19", phrase)  
    phrase = re.sub(r'\bcnn\b', "", phrase)  
    phrase = re.sub(r'\bfox\b', "", phrase)  
    phrase = re.sub(r"\sp.m.\s", " pm ", phrase)
    phrase = re.sub(r"\sa.m.\s", " am ", phrase)
    phrase = re.sub(r"\si.e.\s", " ie ", phrase)
    phrase = re.sub(r"\bjan.\s", " january ", phrase) 
    phrase = re.sub(r"\sfeb.\s", " february ", phrase) 
    phrase = re.sub(r"\smar.\s", " march ", phrase) 
    phrase = re.sub(r"\sapr.\s", " april ", phrase)  
    phrase = re.sub(r"\saug.\s", " august ", phrase) 
    phrase = re.sub(r"\ssept.\s", " september ", phrase) 
    phrase = re.sub(r"\soct.\s", " october ", phrase) 
    phrase = re.sub(r"\snov.\s", " november ", phrase) 
    phrase = re.sub(r"\sdec.\s", " december ", phrase) 
    phrase = re.sub(r'\ssun.\s', " sunday ", phrase) 
    phrase = re.sub(r"\smon.\s", " monday ", phrase)  
    phrase = re.sub(r"\sthurs.\s|\sthur.\s|\sthu.\s", " thursday ", phrase)  
    phrase = re.sub(r"\stues.\s|\stue.\s|\stu.\s", " tuesday ", phrase)  
    phrase = re.sub(r"\swed.\s", "wednesday", phrase) 
    phrase = re.sub(r"\sfri.\s", "friday", phrase) 
    phrase = re.sub(r"\ssat.\s", "saturday", phrase)  
    return phrase

def DataCleaning(s, lst = True): 
    string = cleaningSpecifics(s) 
    string = remove_stopwords(string.lower())
    rgx = re.compile("\b\d+(?:%|percent\b)|(?:\w)+") 
    string = cleaning(string) 
    txt = rgx.findall(string) 
    txt = [Lem.lemmatize(word) for word in txt]    

    if lst == False:
        txt = ' '.join(txt)
    return(txt)

def Lemmatizer(tokens):
    stop_words = stopwords.words('english')
    cleaned_tokens = []

    for token, tag in pos_tag(tokens):
        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        token = Lem.lemmatize(token, pos)

        if len(token) > 1 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

def run(txt):
    return([Lemmatizer(DataCleaning(article)) for article in txt])