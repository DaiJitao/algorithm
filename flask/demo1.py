from typing import List, Optional

from flask import Flask, Request

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, text similarity!'


@app.route('/sim/query')
def hello():
    return 'Hello, query text similarity!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=9962)