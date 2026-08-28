#It's enumerate pracite!

#done!
#v1.0

from time import sleep

tasks = ["Go to grocery shop", "Pass the exam with a score of 100", "Learn python"]

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)

def menu():
    print("=== Tasks ===")
    pause_long()
    print("1️⃣  1. Show tasks")
    pause_short()
    print("2️⃣  2. Complete task")
    pause_short()
    print("3️⃣  3. Exit")
    pause_long()
    menu_choice = input("⌨️  Enter your choice: ").strip()
    pause_long()
    if menu_choice.isdigit():
        continue_menu = False
        menu_choice = int(menu_choice)
        return menu_choice, continue_menu
    elif menu_choice == "":
        continue_menu = True
        print("❗ Choice can't be empty!")
        pause_long()
        return menu_choice, continue_menu
    else:
        continue_menu = True
        print("❗ Choice need to be number!")
        pause_long()
        return menu_choice, continue_menu

def show_tasks(tasks):
    if not tasks:
        print("❗ Your tasks is empty!")
        pause_long()
    else:
        text = ""
        print("📋 Your tasks:")
        pause_long()
        for num, task in enumerate(tasks, 1):
            text = text + f"{num}. {task};\n"
        text = text[0: -2: 1]
        print(text)
        pause_long()

def complete_task(tasks):
    while True:
        if not tasks:
            print("❗ Your tasks is empty!")
            pause_long()
            return tasks  
        print("=== Complete task ===")
        pause_long()
        show_tasks(tasks)
        task_to_complete = input("⌨️  Enter task number to complete it:").strip()
        if task_to_complete.isdigit():
            task_to_complete = int(task_to_complete)
            task_to_complete_index = task_to_complete - 1
            if task_to_complete_index < 0:
                print("❗Not right number of task!")
                pause_long()
                continue
            elif task_to_complete_index >= len(tasks):
                print("❗Not right number of task!")
                pause_long()
                continue
            else:
                task_name = tasks[task_to_complete_index]
                tasks.pop(task_to_complete_index)
                print(f"✅🗑️ Task '{task_name}' completed and deleted!")
                pause_long()
                return tasks
        elif task_to_complete == "":
            print("❗ Task number can't be empty!")
            pause_long()
            continue
        else:
            print("❗ You need to enter number of task!")
            pause_long()
            continue

def exit_program(tasks):
    show_tasks(tasks)
    print("👋 Goodbye!")
    pause_long()

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
            pause_long()
            continue