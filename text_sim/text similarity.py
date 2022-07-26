from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
import nltk
import re
from flask import Flask, jsonify, request
from gensim.models import Word2Vec
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
import pandas as pd
import en_core_web_sm
nlp = en_core_web_sm.load()
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')


def pre_processing(file):
    tokens=word_tokenize(file)
    words=[w.lower() for w in tokens]
    porter=nltk.WordNetLemmatizer()
    lemmatize=[porter.lemmatize(t) for t in words]
    stop_words=set(stopwords.words('english'))
    filtered_tokens=[w for w in lemmatize if not w in stop_words]
    return filtered_tokens


@app.route("/model", methods=["GET","POST"])
def output():
    if request.method == "POST":
        text1 = pre_processing(input())
        text2 = pre_processing(input())
        text1  = " ".join(text1)
        text2  = " ".join(text2)
        vector1 = nlp(text1)
        vector2 = nlp(text2)
        return vector1.similarity(vector2)

if __name__ == "__main__":
     app.run(debug=True)           