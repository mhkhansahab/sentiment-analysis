from flask import Flask
from flask import request
from textblob import TextBlob
import json
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def analyze(data):
    text = data
    blob = TextBlob(text)
    return blob.sentiment

@app.route('/analyze', methods=['POST'])
@cross_origin()
def sentimentAnalyzer():
    if request.method == 'POST':
      data = json.loads(request.get_data())
      analyzed = analyze(data["text"])
      dict = {
          "polarity" : analyzed.polarity,
          "subjectivity" : analyzed.subjectivity
      }
      return json.dumps(dict)

port = int(os.environ.get('PORT', 8000))

if __name__ == "__main__":
    app.run(debug=True, port=port)
