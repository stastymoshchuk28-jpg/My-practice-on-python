#Not done!
#v0.9

from time import sleep

tasks = []

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def check_for_task(tasks, entered_task):
    for task in tasks:
        task_for_check = task.lower().strip()
        if entered_task == task_for_check:
            using_task = task
            return using_task
        else:
            using_task = False
            continue
    return using_task

def show_tasks(tasks):
    if not tasks:
        print("❗ No tasks!")
        oformity1()
    else:
        task_number = 1
        print("📋 Your tasks:")
        oformity1()
        for task in tasks:
            print(f"{task_number}. {task} \n")
            task_number += 1
            oformity2()
        oformity1()
        
def add_task(tasks):
    while True:
        new_task = input("⌨️  Enter new task: ").capitalize()
        oformity1()
        if new_task == "":
            print("❗ Task can't be empty!")
            oformity1()
            continue
        elif new_task.isdigit():
            print("❗ Task can't be only numbers!")
            oformity1()
            continue
        else:
            print("✅ Task added!")
            oformity1()
            tasks.append(new_task)
            return tasks
    
def delete_task(tasks):
    while True:
        text = ""
        print("📋 Your tasks: ", end="")
        for task in tasks:
            text = text + task + "; "
        text = text[0: -2: 1]
        print(text)
        oformity1()
        task_for_delete = input("⌨️  Enter task to delete it: ").strip().lower()
        if task_for_delete == "":
            print("❗ Task can't be empty!")
            oformity1()
            continue
        elif task_for_delete.isdigit():
            print("❗ Task can't be only numbers!")
            oformity1()
            continue
        else:
            task_for_deleting = check_for_task(tasks, task_for_delete)
            if task_for_deleting == False:
                print("❗ Not right name of task!")
                oformity1()
                continue
            else:
                ...


while True:
    print("=== TO-DO LIST ===")
    oformity1()
    print("1️⃣  1. Show tasks")
    oformity2()
    print("2️⃣  2. Add task")
    oformity2()
    print("3️⃣  3. Delete task")
    oformity2()
    print("4️⃣  4. Complete task")
    oformity2()
    print("5️⃣  5. Exit")
    oformity1()
    choice = input("⌨️  Enter your choice: ").lower().strip()
    oformity1()
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            show_tasks(tasks)
        elif choice == 2:
            ...
        elif choice == 3:
            ...
        elif choice == 4:
            ...
        elif choice == 5:
            ...
    elif choice == "":
        print("❗ Choice can't be empty!")
        oformity1()
        continue
    else:
        print("❗ Choice need to be number!")
        oformity1()
        continue
