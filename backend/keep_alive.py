import os
from flask import Flask
from threading import Thread

from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS #comment this on deployment

app = Flask(__name__, static_url_path='', static_folder='../frontend/build')
CORS(app) #comment this on deployment
api = Api(app)

@app.route('/', defaults={'path':''})
def home(path):
    return send_from_directory(app.static_folder,'index.html')


def run():
  port = int(os.environ.get('PORT', 5000))
  if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port)


def keepAlive():
    t = Thread(target=run)
    t.start()
