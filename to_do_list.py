import json
from datetime import datetime

def write_json(data, filename='project_ideas.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)

def addToProjectList(name, description: str = None):
    with open('project_ideas.json') as jsonFile:
        data = json.load(jsonFile)
        temp = data["project_ideas"]
        x = len(temp)

        # append to json array
        new_item = {
            "id": x+1,
            "project_name": name,
            "description": description,
            "start_time": None,
            "end_time": None
        }

        temp.append(new_item)
    write_json(data)

def addToStudyList(name):
    with open('study_list.json') as jsonFile:
        data = json.load(jsonFile)
        temp = data["study_ideas"]
        x = len(temp)

        # append to json array
        new_item = {
            "id": x+1,
            "name": name,
        }

        temp.append(new_item)
    write_json(data)

def updateList(name: str, Description: str = None):
    with open('project_ideas.json', 'r+') as jsonFile:
        data = json.load(jsonFile)
        temp = data["project_ideas"]

        for i in temp:
            if(i["project_name"] == name):
                # update to json array
                i["start_time"] = str(datetime.now())

        jsonFile.seek(0)  # rewind
        json.dump(data, jsonFile)
        jsonFile.truncate()
