#It's enumerate pracite!
from time import sleep

tasks = ["Go to grocery shop", "Pass the exam with a score of 100", "Learn python"]

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def menu():
    print("=== Tasks ===")
    oformity1()
    print("1️⃣  1. Show tasks")
    oformity2()
    print("2️⃣  2. Complete task")
    oformity2()
    print("3️⃣  3. Exit")
    oformity1()
    menu_choice = input("⌨️  Enter your choice: ").strip()
    oformity1()
    if menu_choice.isdigit():
        continue_menu = False
        menu_choice = int(menu_choice)
        return menu_choice, continue_menu
    elif menu_choice == "":
        continue_menu = True
        print("❗ Choice can't be empty!")
        oformity1()
        return menu_choice, continue_menu
    else:
        continue_menu = True
        print("❗ Choice need to be number!")
        oformity1()
        return menu_choice, continue_menu

def show_tasks(tasks):
    if not tasks:
        print("❗ Your tasks is empty!")
        oformity1()
    else:
        text = ""
        print("📋 Your tasks:")
        oformity1()
        for num, task in enumerate(tasks, 1):
            text = text + f"{num}. {task};\n"
        text = text[0: -2: 1]
        print(text)
        oformity1()

def complete_task(tasks):
    while True:
        if not tasks:
            print("❗ Your tasks is empty!")
            oformity1()
            return tasks  
        print("=== Complete task ===")
        oformity1()
        show_tasks(tasks)
        task_to_complete = input("⌨️  Enter task number to complete it:").strip()
        if task_to_complete.isdigit():
            task_to_complete = int(task_to_complete)
            task_to_complete_index = task_to_complete - 1
            if task_to_complete_index < 0:
                print("❗Not right number of task!")
                oformity1()
                continue
            elif task_to_complete_index >= len(tasks):
                print("❗Not right number of task!")
                oformity1()
                continue
            else:
                task_name = tasks[task_to_complete_index]
                tasks.pop(task_to_complete_index)
                print(f"✅🗑️ Task '{task_name}' completed and deleted!")
                oformity1()
                return tasks
        elif task_to_complete == "":
            print("❗ Task number can't be empty!")
            oformity1()
            continue
        else:
            print("❗ You need to enter number of task!")
            oformity1()
            continue

def exit_program(tasks):
    show_tasks(tasks)
    print("👋 Goodbye!")
    oformity1()

while True:
    menu_choice, continue_menu = menu()
    if continue_menu:
        continue
    else:
        if menu_choice == 1:
            show_tasks(tasks)
        elif menu_choice == 2:
            tasks = complete_task(tasks)
        elif menu_choice == 3:
            exit_program(tasks)
            break
        else:
            print("❗ Not right number of choice!")
            oformity1()
            continue