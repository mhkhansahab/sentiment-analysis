from flask import Flask
from flask import request
from textblob import TextBlob
import json

app = Flask(__name__)
def analyze(data):
    text = data
    blob = TextBlob(text)
    return blob.sentiment

@app.route('/analyze', methods=['POST'])
def sentimentAnalyzer():
    if request.method == 'POST':
      data = json.loads(request.get_data())
      analyzed = analyze(data["text"])
      dict = {
          "polarity" : analyzed.polarity,
          "subjectivity" : analyzed.subjectivity
      }
      return dict

if __name__ == "__main__":
    app.run(debug=True, port=8000)
