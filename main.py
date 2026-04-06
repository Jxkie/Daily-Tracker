import json

taskOfDay = []

def openFile():
    global taskOfDay
    try:
        with open("tasks.json", "r") as f:
            taskOfDay = json.load(f)
    except:
        with open("tasks.json", "x") as f:
            pass

def closeFile():
    global taskOfDay
    with open("tasks.json", "w") as f:
        json.dump(taskOfDay, f)

def addTask():
    title = input("Название задачи:")
    time = input("Время задачи:")
    task = {
        "taskName": title,
        "taskTime": time,
        "taskStatus": False
    }
    taskOfDay.append(task)
    closeFile()
    return taskOfDay

def displayTasks():
    for i, tasks in enumerate(taskOfDay, 1):
        print(f"{i}. {tasks['taskName']} --- {tasks['taskTime']} - status: {tasks['taskStatus']}")

openFile()
while(True):
    print(f"Задачи")
    print(f"----------------------------------------\n ")
    displayTasks()
    print(f"\n----------------------------------------")
    print(f"1. Добавть задачу. 2. Удалить задачу. 3. Закрыть приложение")
    choose = int(input("Выбери действие: "))
    match choose: 
        case 1:
            addTask()
        case 2:
            pass
        case 3:
            quit()
        case _: 
            pass