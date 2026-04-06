import json

taskOfDay = []

try:
    with open("tasks.json", "r") as f:
        taskOfDay = json.load(f)
except:
    with open("tasks.json", "x") as f:
        pass

def addTask(title, time):
    task = {
        "taskName": title,
        "taskTime": time,
        "taskStatus": False
    }
    taskOfDay.append(task)
    return taskOfDay

title = input("Название задачи:")
time = input("Время задачи:")

addTask(title, time)

with open("tasks.json", "w") as f:
    json.dump(taskOfDay, f)

print(taskOfDay)