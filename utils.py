import re

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

