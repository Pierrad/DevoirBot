
import requests
from datetime import datetime
import uuid
import json


class APIHandler:

	def __init__(self, apiToken, apiUrl):
		self.apiToken = apiToken
		self.apiUrl = apiUrl

	def getProjectList(self):
		projectList = requests.get("%s/projects" % self.apiUrl,
		headers={
		"Authorization":
		"Bearer %s" % self.apiToken
		}).json()
		return projectList

	def getProjectIDByName(self, projectName):
		projectList = self.getProjectList()
		projectIdFromName = list((project['id'] for project in projectList if project['name'] == projectName))[0]
		print(projectIdFromName)
		return str(projectIdFromName)

	def createProject(self, projectName):
		self.api.projects.add(projectName)
		self.api.commit()
		return True

	def getAllTasks(self):
		tasksList = requests.get("%s/tasks" % self.apiUrl,
		headers={
		"Authorization":
		"Bearer %s" % self.apiToken
		}).json()
		return tasksList

	def getTodayTasks(self):
		allTasks = self.get_allTasks()
		todayTasks = []

		today = datetime.today().date()
		for task in allTasks:
			taskDue = task.get('due')
		if taskDue:
			taskDueDateString = taskDue.get('date')
			taskDueDate = datetime.strptime(taskDueDateString,'%Y-%m-%d').date()
		if taskDueDate == today:
			todayTasks.append(task)

		return todayTasks

	def createTask(self, task_content):
		result = requests.post("%s/tasks" % self.apiUrl,
		data=json.dumps({
		"content": task_content,
		}),
		headers={
		"Content-Type": "application/json",
		"X-Request-Id": str(uuid.uuid4()),
		"Authorization": "Bearer %s" % self.apiToken
		}).json()

		return result
