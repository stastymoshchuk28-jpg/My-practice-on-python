#Not Done
#v0.5

from time import sleep, ctime

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)

def start_work(user_info):
    while True:
        print("=== Welcome to Myrchik OS! ===")
        pause_long()
        print("Let's create your account!")
        pause_long()
        user_name = input("Enter username for account: ").strip()
        pause_long()
        if user_name == "":
            print("ERROR OF ACCOUNT CREATING:")
            pause_long()
            print("user_info: user_name -- ''\nEMPTY USERNAME -- user_info error!\nError code: INFO-USER.XXX-USERNAMEerr")
            pause_long()
            print("Restarting start_work_script...")
            pause_long()
            continue
        else:
            print("INFO-USER.XXX-USERNAME.SAVED")
            pause_long()
            user_info["user_name"] = user_name
            need_password = input("Do you need password (Recommend to save your computer from hackers)? (y/n)").strip().lower()
            pause_long()
            if need_password == "":
                print("ERROR OF ACCOUNT CREATING:")
                pause_long()
                print("user_info: need_password -- ''\nEMPTY CHOICE OF SAFITY -- user_info error!\nError code: INFO-USER.XXX-SAFITYerr")
                pause_long()
                print("Restarting start_work_script...")
                pause_long()   
                continue
            else:
                if need_password == "y":
                    print("Safity_script on!")
                    pause_long()
                    password = input("Enter password for your system: ").strip()    
                    pause_long()     
                    if password == "":
                        print("ERROR OF ACCOUNT CREATING:")
                        pause_long()
                        print("user_info: password -- ''\nEMPTY PASSWORD -- user_info error!\nError code: INFO-USER.XXX-.Safity_script.-PASSWORDerr")
                        pause_long()
                        print("Restarting start_work_script...")
                        pause_long()   
                        continue
                    else:
                        print(f"Password {password} saved!")
                        pause_long()
                        user_info["password"] = password
                elif need_password == "n":
                    print("Safity_script_start off!")
                    pause_long()
                else:
                    print("ERROR OF ACCOUNT CREATING:")
                    pause_long()
                    print("user_info: need_password -- ''\nCHOICE OF SAFITY ERROR -- user_info error!\nError code: INFO-USER.XXX-SAFITYerr")
                    pause_long()
                    print("Restarting start_work_script...")
                    pause_long()   
                    continue
                print("End creating account for Myrchik OS!")
                pause_long()
                print("Enter command 'help' to see commands list or 'stop' to end your work!")
                pause_long()
                return user_info

def command_list_show():
    print("Commands list: ")
    pause_long()
    for c in commands.keys():
        print(c)
        pause_short()
    pause_long()

def show_user():
    print("Myrchik OS user: ")
    pause_long()
    print(f"Username: {user_info["user_name"]}")
    pause_short()
    if user_info["password"] == None:
        print("Password: NO PASSWORD")
        pause_long()
    else:
        print(f"Password: {user_info["password"]}")
        pause_long()

def show_time():
    current_time = ctime()
    print(f"Current time: {current_time}")
    pause_long()

def stop_work():
    print("Thanks for using Myrchik OS!")
    pause_long()
    print("Goodbye!")
    exit()


commands = {
    "help": command_list_show,
    "whoami": show_user,
    "time": show_time,
    "stop": stop_work
}

user_info = {
    "user_name": None,
    "password": None
}

user_info = start_work(user_info)

while True:
    command = input("Enter name of command ('help' to see commands list): ").strip().lower()
    pause_long()
    if command in commands:
        command_to_enter = commands[command]
        command_to_enter()
    else:
        print("ERROR OF OS-TERMINAL-COMMAND_NOT_FOUND:")
        pause_long()
        print(f"OS-TERMINAL: COMMAND_NOT_FOUND -- '{command} not in commands list!'\n -- OS-TERMINAL-COMMAND_NOT_FOUND error!\nError code: OS-.CORE_FOLDER.-TERMINAL.XXX-.COMMAND_NOT_FOUNDerr.-OS_ERROR")
        pause_long()
        print("Restarting terminal...")
        pause_long()
        continue