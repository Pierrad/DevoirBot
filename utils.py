import re
from datetime import date, timedelta, datetime


def extractFromMessage(message, api):
    task = re.findall('"([^"]*)"',  message.content)
    
    projectID = extractProjectFromMessage(task, api)
    taskContent = extractContentFromMessage(task)
    dueDate = extractDateFromMessage(task)
    
    return (projectID, taskContent, dueDate)

def extractProjectFromMessage(messageList, api):
    projectID = api.getProjectIDByName(messageList[0])
    return projectID

def extractContentFromMessage(messageList):
    return messageList[1]

def extractDateFromMessage(messageList):
    dueDate = ""
    if len(messageList) > 2:
        dueDate = messageList[2]
    return correctDateIfNecessary(dueDate)

def correctDateIfNecessary(dueDate):
    if "/" in dueDate:
        dueDate = dueDate.replace("/", "-")
    return dueDate


def writeTaskToLogFile(task):
    taskFileLog = open("taskLog.txt", "a+")
    taskFileLog.write(str(task.get("id")) + " " + str(task.get("due").get("date")) + "\n")
    taskFileLog.close()


def saveIdToFileNotifier(id):
    notifierFile = open("notifier.txt", "r+")
    lines = notifierFile.readlines()
    for line in lines:
        print(line)
        if (line == str(id) + "\n"):
            return False
    notifierFile.write(str(id) + "\n")
    notifierFile.close()
    return True

def removeIdToFileNotifier(id):
    notifierFile = open("notifier.txt", "r")
    lines = notifierFile.readlines()
    notifierFile.close()

    notifierFile = open("notifier.txt", "w")
    for line in lines:
        if (line != str(id) + "\n"):
            notifierFile.write(str(id) + "\n")
    
    return True

def getNotifier():
    notifierFile = open("notifier.txt", "r")
    notifier = ""
    for line in notifierFile.readlines():
        lineWithoutCariage = line.replace("\n", "")
        notifier += f"<@{lineWithoutCariage}>, "
    return notifier

def checkForNextTask(dueDate = ""):
    if dueDate == "":
        dateNow = date.today()
        delay = timedelta(days=1)
        dueDate = dateNow + delay
    taskFile = open("taskLog.txt", "r")
    tasks = []
    for line in taskFile.readlines():
        if str(dueDate) in line:
            tasks.append(line.split(" ")[0])
    return tasks

def formatTasksOutput(tasks):
    output = ""
    for task in tasks:
        output += "- En " + task[0] + ", il faut : " + task[1] + " pour le " + task[2] + "\n"
    return output

def removePastTasks():
    dateNow = date.today()
    taskFileLog = open("taskLog.txt", "r")
    removeTasks = []
    for line in taskFileLog.readlines():
        if dateNow > datetime.strptime(line.split(" ")[1], '%y-%m-%d'):
            removeTasks.append(line)
    taskFileLog.close()
    
    taskFileLog = open("taskLog.txt", "w")
    for line in taskFileLog.readlines:
        for task in removeTasks:
            if line != task:
                taskFileLog.write(line)
    taskFileLog.close()
