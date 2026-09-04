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
            need_password = False
            while True:
                need_password = input("Do you need password (Recommend to save your computer from hackers)? (y/n) ").strip().lower()
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
                        need_password = True
                        pause_long()
                        break
                    elif need_password == "n":
                        print("start_work:safity_choice_script--Safity_script_start off!")
                        need_password = False
                        pause_long()
                    else:
                        print("ERROR OF ACCOUNT CREATING:")
                        pause_long()
                        print("user_info: need_password -- ''\nCHOICE OF SAFITY ERROR -- user_info error!\nError code: INFO-USER.XXX-SAFITYerr")
                        pause_long()
                        print("Restarting start_work:safity_choice_script...")
                        pause_long()   
                        continue
            if need_password:
                while True:
                    password = input("Enter password for your system: ").strip()    
                    pause_long()     
                    if password == "":
                        print("ERROR OF ACCOUNT CREATING:")
                        pause_long()
                        print("user_info: password -- ''\nEMPTY PASSWORD -- user_info error!\nError code: INFO-USER.XXX-.Safity_script.-PASSWORDerr")
                        pause_long()
                        print("Restarting start_work:safity_choice_script...")
                        pause_long()   
                        continue
                    else:
                        print(f"Password {password} saved!")
                        pause_long()
                        user_info["password"] = password
                    print("End creating account for Myrchik OS!")
                    pause_long()
                    print("Enter command 'help' to see commands list or 'stop' to end your work!")
                    pause_long()
            else:
                print("End creating account for Myrchik OS!")
                pause_long()
                print("Enter command 'help' to see commands list or 'stop' to end your work!")
                pause_long()                
            return user_info

def command_list_show(user_info, commands):
    print("Commands list: ")
    pause_long()
    standart_user_commands = commands["standart_user_commands"]
    for c in standart_user_commands.keys():
        print(f"'{c}'")
    pause_long()
    if user_info["super_user"]:
        super_user_commands = commands["super_user_commands"]
        print("Super user commands list: ")
        for c in super_user_commands.keys():
            print(f"'{c}'")
        pause_long()
        print("Use super user commands with caution! It's can delete your user info or even system!")
    pause_long()

def show_user(user_info):
    print("Myrchik OS user: ")
    pause_long()
    if user_info["user_name"] == None:
        print("Username: USER_NOT_FOUND -- NONE_USER -- USER_DELETED or WORK_NOT_STARTED! Please restart your system to create new user!")
        pause_short()
    else:
        print(f"Username: {user_info["user_name"]}")
        pause_short()
    if user_info["password"] == None:
        print("Password: NO PASSWORD")
        pause_long()
    else:
        print(f"Password: {user_info['password']}")
        pause_long()

def show_time():
    current_time = ctime()
    print(f"Current time: {current_time}")
    pause_long()

def make_super_user(user_info):
    if user_info["user_name"] != None and user_info["password"] != None:
        if user_info["super_user"]:
            print("You are already super user!")
            pause_long()
        else:
            print("Now you are super user! Unlocked administator commands!")
            user_info["super_user"] = True
            pause_long()
    else:
        print("USER: USER_INFO -- user_name = None, password = None: NOT FOUND USER!")
    return user_info

def make_standart_user(user_info):
    if not user_info["super_user"]:
        print("You are already standart user!")
        pause_long()
    else:
        print("Now you are standart user! Blocked administator commands!")
        user_info["super_user"] = False
        pause_long()
    return user_info

def delete_user(user_info):
    if user_info["user_name"] != None and user_info["password"] != None:
        while True:
            sure_to_delete = False
            if user_info["password"] != None:
                enter_password = input("Enter your password to check your indentify: ").strip()
                pause_long()
                if enter_password == user_info["password"]:
                    print("Identify checked!")
                    pause_long()
                else:
                    print("Identify declined!")
                    pause_long()
                    return user_info()
            sure = input("Are you sure to delete user? (y/n) ").strip().lower()
            pause_long()
            if sure == "y":
                sure_to_delete = True
                break
            elif sure == "n":
                print("Delete_user_script off!")
                pause_long()
                break
            else:
                print("ERROR OF USER ACCOUNT DELETING:")
                pause_long()
                print("user_info_delete: sure_to_delete -- ''\nEMPTY OR NOT RIGHT CHOICE OF SURE_TO_DELETE_CHOICE -- user_info_delete error!\nError code: INFO-USER.XXX==SUDO_ADMIN==-CHOICE.SURE.TO.DELETEerr")
                pause_long()
                print("Restarting delete_user_info_script...")
                pause_long()
                continue
        if sure_to_delete:
            user_info["user_name"] = None
            user_info["password"] = None
            user_info["super_user"] = False
            print("User deleted!")
            pause_long()
        return user_info
    else:
        print("USER: USER_INFO -- user_name = None, password = None: NOT FOUND USER!")
        pause_long()
        return user_info
        
def stop_work():
    print("Thanks for using Myrchik OS!")
    pause_long()
    print("Goodbye!")
    pause_long()
    exit()

user_info = {
    "user_name": None,
    "password": None,
    "super_user": False
}

commands = {
    "standart_user_commands":{
        "help": lambda: command_list_show(user_info, commands),
        "whoami": lambda: show_user(user_info),
        "time": show_time,
        "stop": stop_work,
        "sudo": lambda: make_super_user(user_info),
        "de_sudo": lambda: make_standart_user(user_info)
    },
    "super_user_commands":{
        "delete_user": lambda: delete_user(user_info)
    }
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