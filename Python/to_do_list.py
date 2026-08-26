#done!
#v1.0

from time import sleep

tasks = []

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def show_tasks_for_functions(tasks):
    text = ""
    print("📋 Your tasks: ", end="")
    task_num = 1
    for task in tasks:
        task_to_show = task[0]
        complete_mark = task[1]
        if complete_mark:
            completed = "✅"
        else:
            completed = "❌"
        text = text + f"{task_num}. " + completed + " " + task_to_show + "; "
        task_num += 1
    text = text[0: -2: 1]
    print(text)
    oformity1()

def show_tasks(tasks):
    if not tasks:
        print("❗ No tasks!")
        oformity1()
    else:
        task_number = 1
        print("📋 Your tasks:")
        oformity1()
        for task in tasks:
            mark_complete = task[1]
            if mark_complete:
                completed = "✅"
            else:
                completed = "❌"
            print(f"{task_number}. {completed} {task[0]} \n")
            task_number += 1
            oformity2()
        print("✅ - completed task, ❌ - not completed task!")
        oformity1()
        
def add_task(tasks):
    while True:
        new_task = input("⌨️  Enter new task: ").strip().capitalize()
        mark_complete = False
        task_in_list = False
        for task in tasks:
            task = task[0]
            task_for_check_in_tasks = task.strip()
            if new_task == task_for_check_in_tasks:
                task_in_list = True
                break
            elif new_task != task_for_check_in_tasks:
                task_in_list = False
                continue
        oformity1()
        if task_in_list:
            print("📋 Task in list alredy!")
            oformity1()
            continue
        else:
            if new_task == "":
                print("❗ Task can't be empty!")
                oformity1()
                continue
            elif new_task.isdigit():
                print("❗ Task can't be only numbers!")
                oformity1()
                continue
            else:
                task_to_add = [new_task, mark_complete]
                print("✅ Task added!")
                oformity1()
                tasks.append(task_to_add)
                print(tasks)
                return tasks
    
def delete_task(tasks):
    while True:
        if not tasks:
            print("❗ No tasks to delete!")
            oformity1()
            return tasks
        else:
            show_tasks_for_functions(tasks)
            task_for_delete = input("⌨️  Enter task number to delete it: ").strip()
            if task_for_delete == "":
                print("❗ Task can't be empty!")
                oformity1()
                continue
            elif task_for_delete.isdigit():
                task_for_delete = int(task_for_delete)
                if task_for_delete > len(tasks):
                    print("❗ Not right number of task!")
                    oformity1()
                    continue
                delete_index = task_for_delete - 1
                if delete_index < 0:
                    print("❗ Not right number of task!")
                    oformity1()
                    continue
                else:
                    task_l = tasks[delete_index]
                    task = task_l[0]
                    tasks.pop(delete_index)
                    print(f"🗑️ Task '{task}' deleted!")
                    oformity1()
                    return tasks
            else:
                print("❗ Task number need to be a digit!")
                oformity1()
                continue

def complete_task(tasks):
    while True:
        if not tasks:
            print("❗ No tasks to mark as completed!")
            oformity1()
            return tasks
        else:
            show_tasks_for_functions(tasks)
            task_to_mark_completed = input("⌨️  Enter task number to mark it as completed: ").strip()
            if task_to_mark_completed == "":
                print("❗ Task can't be empty!")
                oformity1()
                continue
            elif task_to_mark_completed.isdigit():
                task_to_mark_completed = int(task_to_mark_completed)
                if task_to_mark_completed > len(tasks):
                    print("❗ Not right number of task!")
                    oformity1()
                    continue
                complete_index = task_to_mark_completed - 1
                if complete_index < 0:
                    print("❗ Not right number of task!")
                    oformity1()
                    continue
                else:
                    task_l = tasks[complete_index]
                    finding_task_c = tasks[complete_index][1]
                    if finding_task_c:
                        print("❗ Task alredy marked as completed!")
                        oformity1()
                        continue
                    else:
                        tasks[complete_index][1] = True
                        print(f"✅ Task: {task_l[0]} has been marked as completed!")
                        oformity1()
                        return tasks
            else:
                print("❗ Task number need to be a digit!")
                oformity1()
                continue

def exit_proggram(tasks):
    show_tasks(tasks)
    print("👋 Goodbye!")
    print(" ")
    exit()

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
            tasks = add_task(tasks)
        elif choice == 3:
            tasks = delete_task(tasks)
        elif choice == 4:
            tasks = complete_task(tasks)
        elif choice == 5:
            exit_proggram(tasks)
    elif choice == "":
        print("❗ Choice can't be empty!")
        oformity1()
        continue
    else:
        print("❗ Choice need to be number!")
        oformity1()
        continue
