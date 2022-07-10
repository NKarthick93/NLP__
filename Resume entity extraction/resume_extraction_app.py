from flask import Flask, jsonify, request
import docx2txt
import re
import string
from pdfminer.high_level import extract_text
app = Flask(__name__)

## Extracting pdf and docx to text
@app.route("/getfile", methods=["POST"])
def getfile():
    if request.method == "POST":
        file = request.files["file"]
        file.save(file.filename)
        if file.filename.endswith(".docx"):
            text = docx2txt.process(file.filename)
        elif file.filename.endswith(".pdf"):
            text = extract_text(file.filename)
        else:
            return "File extension not supported"
        text = re.sub('\n', ' ', text)
        text = re.sub('\s+', ' ', text)
        text = re.sub('\s+', ' ', text)
        text = text.replace('•', '', -1) 
        text = re.sub(' +', ' ', text)
        return jsonify({"text": text})
    else:
        return "Only POST requests are supported"

if __name__ == "__main__":
    app.run(debug=True)  