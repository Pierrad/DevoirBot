from backend.APIHandler import APIHandler
import os
from flask import Flask
from threading import Thread

from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS, cross_origin #comment this on deployment
from dotenv import load_dotenv

load_dotenv()

todo = APIHandler(os.environ['TODOIST_API'], "https://api.todoist.com/rest/v1")

app = Flask(__name__, static_url_path='', static_folder='../frontend/build')
CORS(app) #comment this on deployment
api = Api(app)

@app.route('/', defaults={'path':''})
@cross_origin()
def home(path):
    return send_from_directory(app.static_folder,'index.html')


def run():
  port = int(os.environ.get('PORT', 5000))
  app.run(threaded=True, host='0.0.0.0',port=port)


def keepAlive():
    t = Thread(target=run)
    t.start()

@app.route('/test')
@cross_origin()
def get():
    return {
      'resultStatus': 'SUCCESS',
      'message': "Hello Api Handler"
      }

@app.route('/allProject')
@cross_origin()
def getAllProject():
  return {'response': todo.getProjectList()} 

@app.route('/projectWithTask')
@cross_origin()
def getAllTasks():
  allTask = todo.getAllTasks()
  res = {}
  for task in allTask:
    if task['project_id'] not in res:
      res[task['project_id']] = {'name': todo.getProjectNameById(task['project_id']), 'tasks': [{'id': task['id'], 'date': task['due']['date'], 'content': task['content']}]}
    else:
      res[task['project_id']]['tasks'].append({'id': task['id'], 'date': task['due']['date'], 'content': task['content']})

  return {'response': res}