#!pip install transformers
#!pip install flair
#!pip install pdfminer.six
#!pip install docx2txt==0.8

from flair.data import Sentence
from flair.models import SequenceTagger
from flask import Flask, jsonify, request
import pandas as pd
import io
import numpy
import ast
import csv
from io import StringIO
import docx2txt
from pdfminer.high_level import extract_text

app = Flask(__name__)

#Extracting entities
def flair_ner(document):
  sentence = Sentence(document)
  tagger = SequenceTagger.load('ner')
  tagger.predict(sentence)
  entities = sentence.to_dict(tag_type='ner')
  return [(entity.pop("text"),entity.pop("labels")) for entity in entities["entities"]]
  
#Converting Dataframe to csv
def csv(file):
    f = flair_ner(file)
    df = pd.DataFrame(f)
    csv = df.to_csv(mode='a',header=False,index=False)
    return csv
    
# Api function
@app.route("/flair_model", methods=["GET","POST"])
def flair_model():
    if request.method == "POST":
        file = request.files["file"]
        file.save(file.filename)
        if file.filename.endswith(".docx"):
            text = docx2txt.process(file.filename)
        elif file.filename.endswith(".pdf"):
            text = extract_text(file.filename)
        else:
            return "File extension not supported"
        file = csv(text)
        # save mutiple file in same file
        with open(r'file.csv', 'a', encoding="utf-8") as f:
            f.write(file)
        return file

if __name__ == "__main__":
     app.run(debug=True)      