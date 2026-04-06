import json
from datetime import datetime

taskOfDay = []

def openFile():
    global taskOfDay
    try:
        with open("tasks.json", "r") as f:
            taskOfDay = json.load(f)
    except FileNotFoundError:
        with open("tasks.json", "x") as f:
            pass


def closeFile():
    global taskOfDay
    with open("tasks.json", "w") as f:
        json.dump(taskOfDay, f)


def addTask():
    title = input("Название задачи:")
    time = input("Время задачи:")
    
    try:
        datetime.strptime(time, "%H:%M")
    except ValueError:
        print(f"Формат времени - hh:mm")
        return
        

    task = {
        "taskName": title,
        "taskTime": time,
        "taskStatus": False
    }
    taskOfDay.append(task)
    closeFile()
    return taskOfDay


def removeTask():
    num = int(input("Выбери номер задачи для удаления: "))
    taskOfDay.pop(num - 1)
    closeFile()
    return taskOfDay


def displayTasks():
    for i, tasks in enumerate(taskOfDay, 1):
        status = "✓" if tasks['taskStatus'] else "✗"
        print(f"{i}. {tasks['taskName']} --- {tasks['taskTime']} - [{status}]")


openFile()
while(True):
    print(f"Задачи")
    print(f"----------------------------------------\n ")
    displayTasks()
    print(f"\n----------------------------------------")
    print(f"1. Добавть задачу. 2. Удалить задачу. 3. Закрыть приложение")
    try: 
        choose = int(input("Выбери действие: "))
    except ValueError:
        print(f"Введи цифру")
        continue
    match choose: 
        case 1:
            addTask()
        case 2:
            displayTasks()
            removeTask()
        case 3:
            quit()
        case _: 
            pass