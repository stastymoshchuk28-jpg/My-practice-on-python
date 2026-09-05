#Not Done
#v0.5

from time import sleep, ctime

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)

def show_error(errors:dict, error_value:str, command=""):
    error = errors[error_value]
    type_error = error["type_of_error"]
    desc = error["description"].format(command)
    rest = error["restart"]
    print(type_error)
    pause_long()
    print(desc)
    pause_long()
    print(rest)
    pause_long()     
    
def start_work(user_info:dict, errors:dict):
    while True:
        print("=== Welcome to Myrchik OS! ===")
        pause_long()
        print("Let's create your account!")
        pause_long()
        user_name = input("Enter username for account: ").strip()
        pause_long()
        if user_name == "":
            show_error(errors, "empty_user_name")
            continue
        else:
            print("INFO-USER.XXX-USERNAME.SAVED")
            pause_long()
            user_info["user_name"] = user_name
            user_name_split = user_name.split()
            for word in user_name_split:
                if word.lower() == "sudo" or word.lower() == "myrchik":
                    user_info["super_user"] = True
                    break
            need_password = False
            while True:
                need_password = input("Do you need password (Recommend to save your computer from hackers)? (y/n) ").strip().lower()
                pause_long()
                if need_password == "":
                    show_error(errors, "empty_need_password")
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
                        break
                    else:
                        show_error(errors, "choice_safity_error")
                        continue
            if need_password:
                while True:
                    password = input("Enter password for your system: ").strip()    
                    pause_long()     
                    if password == "":
                        show_error(errors, "empty_password")  
                        continue
                    else:
                        print(f"Password {password} saved!")
                        pause_long()
                        user_info["password"] = password
                    print("End creating account for Myrchik OS!")
                    pause_long()
                    print("Enter command 'help' to see commands list or 'stop' to end your work!")
                    pause_long()
                    break
            else:
                print("End creating account for Myrchik OS!")
                pause_long()
                print("Enter command 'help' to see commands list or 'stop' to end your work!")
                pause_long()                
            return user_info

def command_list_show(user_info:dict, commands:dict):
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

def show_user(user_info:dict):
    print("Myrchik OS user: ")
    pause_long()
    if user_info["user_name"] is None:
        print("Username: USER_NOT_FOUND -- NONE_USER -- USER_DELETED or WORK_NOT_STARTED! Please restart your system to create new user!")
        pause_short()
    else:
        print(f"Username: {user_info["user_name"]}")
        pause_short()
    if user_info["password"] is None:
        print("Password: NO PASSWORD")
        pause_long()
    else:
        print(f"Password: {user_info['password']}")
        pause_long()
    print(f"Super user: {user_info['super_user']}")
    pause_long()

def show_time():
    current_time = ctime()
    print(f"Current time: {current_time}")
    pause_long()

def make_super_user(user_info:dict):
    if user_info["user_name"] is not None:
        if user_info["super_user"]:
            print("You are already super user!")
            pause_long()
        else:
            print("Now you are super user! Unlocked administator commands!")
            user_info["super_user"] = True
            pause_long()
    else:
        print("USER: USER_INFO -- user_name = None: NOT FOUND USER!")
    return user_info

def make_standart_user(user_info:dict):
    if user_info["user_name"] is not None:
        if not user_info["super_user"]:
            print("You are already standart user!")
            pause_long()
        else:
            print("Now you are standart user! Blocked administator commands!")
            user_info["super_user"] = False
            pause_long()
    else:
        print("USER: USER_INFO -- user_name = None: NOT FOUND USER!")
    return user_info

def delete_user(user_info:dict, errors:dict):
    if user_info["user_name"] is not None:
        while True:
            sure_to_delete = False
            if user_info["password"] is not None:
                enter_password = input("Enter your password to check your indentify: ").strip()
                pause_long()
                if enter_password == user_info["password"]:
                    print("Identify checked!")
                    pause_long()
                else:
                    print("Identify declined!")
                    pause_long()
                    return user_info
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
                show_error(errors, "delete_user_not_right_choice")
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
        "delete_user": lambda: delete_user(user_info, errors)
    }
}

errors = {
        "empty_user_name": {
            "type_of_error": "ERROR OF ACCOUNT CREATING:",
            "description": "user_info: user_name -- ''\nEMPTY USERNAME -- user_info error!\nError code: INFO-USER.XXX-USERNAMEerr",
            "restart": "Restarting start_work_script..."
        },
        "empty_need_password": {
            "type_of_error": "ERROR OF ACCOUNT CREATING:",
            "description": "user_info: need_password -- ''\nEMPTY CHOICE OF SAFITY -- user_info error!\nError code: INFO-USER.XXX-SAFITYerr",
            "restart": "Restarting start_work_script--NEED_PASSWORD_CHOICE..."
        },
        "choice_safity_error": {
            "type_of_error": "ERROR OF ACCOUNT CREATING:",
            "description": "user_info: need_password -- ''\nCHOICE OF SAFITY ERROR -- user_info error!\nError code: INFO-USER.XXX-SAFITYerr",
            "restart": "Restarting start_work:safity_choice_script..."
        },
        "empty_password": {
            "type_of_error": "ERROR OF ACCOUNT CREATING:",
            "description": "user_info: password -- ''\nEMPTY PASSWORD -- user_info error!\nError code: INFO-USER.XXX-.Safity_script.-PASSWORDerr",
            "restart": "Restarting start_work:--SAFITY_SCRIPT--:safity_._script_._password_inputter..."
        },
        "delete_user_not_right_choice": {
            "type_of_error": "ERROR OF USER ACCOUNT DELETING:",
            "description": "user_info_delete: sure_to_delete -- ''\nEMPTY OR NOT RIGHT CHOICE OF SURE_TO_DELETE_CHOICE -- user_info_delete error!\nError code: INFO-USER.XXX==SUDO_ADMIN==-CHOICE.SURE.TO.DELETEerr",
            "restart": "Restarting delete_user_info_script..."
        },
        "command_not_found": {
            "type_of_error": "ERROR OF OS-TERMINAL-COMMAND_NOT_FOUND:",
            "description": "OS-TERMINAL: COMMAND_NOT_FOUND -- '{} not in commands list!'\n -- OS-TERMINAL-COMMAND_NOT_FOUND error!\nError code: OS-.CORE_FOLDER.-TERMINAL.XXX-.COMMAND_NOT_FOUNDerr.-OS_ERROR",
            "restart": "Restarting terminal..."
        },
        "command_blocked": {
            "type_of_error": "ERROR OF OS-TERMINAL-COMMAND_BLOCKED:",
            "description": "OS-TERMINAL: COMMAND_BLOCKED -- '{} -- BLOCKED -- USER_INFO:super_user = False!'\n -- OS-TERMINAL-COMMAND_BLOCKED error!\nError code: OS-.CORE_FOLDER.-TERMINAL.XXX-.COMMAND_BLOCKEDerr.-OS_ERROR",
            "restart": "Restarting terminal..."
        },
        "no_user_error": {
            "type_of_error": "CRITICAL ERROR OF OS-TERMINAL-==NO_USER==:",
            "description": "OS-TERMINAL: ==the_doesn't_have_user_error== -- '{} -- USAGE IS BLOCKED -- OS-.CORE_FOLDER.-TERMINAL.XXX-.NO_USER_ERROR==CRITICAL==e.r.r!'\n -- OS-TERMINAL-NO_USER critical error!\nError code: OS-.CORE_FOLDER.-TERMINAL.XXX-.NO_USER_ERROR==CRITICAL==e.r.r",
            "restart": "Restarting Myrchik OS..."
        },
}

user_info = start_work(user_info, errors)

while True:
    command = input("Enter name of command ('help' to see commands list): ").strip().lower()
    pause_long()
    if user_info["user_name"] is None:
        if command == "stop":
            command_to_enter = commands["standart_user_commands"][command]
            command_to_enter()      
        else:
            show_error(errors, "no_user_error", command)
            user_info = start_work(user_info, errors)
            continue   
    else:
        if command in commands["standart_user_commands"]:
            command_to_enter = commands["standart_user_commands"][command]
            command_to_enter()           
        elif command in commands["super_user_commands"] and user_info["super_user"]:
            command_to_enter = commands["super_user_commands"][command]
            command_to_enter()
        else:
            if not command in commands["standart_user_commands"] and not command in commands["super_user_commands"]:
                show_error(errors, "command_not_found", command)
                continue
            elif command in commands["super_user_commands"] and not user_info["super_user"]:
                show_error(errors, "command_blocked", command)
                continue