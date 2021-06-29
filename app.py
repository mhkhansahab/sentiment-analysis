from flask import Flask
from flask import request
from flask import Response
from textblob import TextBlob
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/analyze": {"origins": "*"}})

def analyze(data):
    blob = TextBlob(data)
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
      resp = Response(json.dumps(dict))
      resp.headers['Access-Control-Allow-Origin'] = '*'
      resp.headers['Content-Type'] = 'application/json'
      return resp

port = int(os.environ.get('PORT', 8000))

if __name__ == "__main__":
    app.run(debug=True, port=port)
