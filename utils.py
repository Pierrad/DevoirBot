import re


def extractFromMessage(message, api):
    task = re.findall('"([^"]*)"',  message.content)
    
    taskContent = extractContentFromMessage(task)
    projectID = extractProjectFromMessage(task, api)
    
    return (taskContent, projectID)

def extractContentFromMessage(messageList):
    return messageList[0]

def extractProjectFromMessage(messageList, api):
    projectID = ""
    if len(messageList) > 1:
        projectID = api.getProjectIDByName(messageList[1])
    return projectID
    