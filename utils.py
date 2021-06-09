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