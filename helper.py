import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
nltk.download('stopwords')

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)         # remove punctuation
    text = re.sub(r'\d+', '', text)             # remove numbers
    text = re.sub(r'\s+', ' ', text).strip()    # remove extra spaces
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')]) # remove stopwords
    return text

def preprocess_input(text):
    text = preprocess(text)         # this is the same preprocess function we defined earlier
    tokens = word_tokenize(text) 
    return tokens
