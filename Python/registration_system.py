#done!
#v1.0
from time import sleep

account = {
    "Username": None,
    "Password": None,
}

have_account = False
log_in_to_account = False

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)

def menu():
    print("=== Registration System ===")
    pause_long()
    print("1️⃣  Create account")
    pause_short()
    print("2️⃣  Log in to account")
    pause_short()
    print("3️⃣  Log out from account")
    pause_short()
    print("4️⃣  Exit")
    pause_long()

def registration_account(account:dict, have_account:bool):
    while True:
        if not have_account:
            user_name = input("⌨️  Enter username for account: ").strip()
            pause_long()
            if user_name == "":
                print("❗ Username can't be empty!")
                pause_long()
                continue
            elif user_name.isdigit():
                print("❗ Username can't be just numbers!")
                pause_long()
                continue
            else:
                print("✅ Username saved!")
                pause_long()
            password = input("⌨️  Enter password for account: ").strip()
            if password == "":
                print("❗ Password can't be empty!")
                pause_long()
                continue
            elif password.isdigit():
                print("❗ Password can't be just numbers!")
                pause_long()
                continue
            else:
                print("✅ Password saved!")
                pause_long()
            account.update(Username=user_name, Password=password)
            have_account = True
            print("✅ Account created!")
            pause_long()
            return account, have_account
        else:
            print("❗ You already have account!")
            pause_long()
            return account, have_account
        
def log_in(account:dict, log_in_to_account:bool):
    while True:
        if account["Username"] != None and account["Password"] != None:
            if log_in_to_account == False:
                print("⚙️ Log in to account:")
                pause_long()
                user_name_to_log_in = input("⌨️  Enter username of account to log in: ").strip()
                pause_long()
                if user_name_to_log_in == account["Username"]:
                    print("✅ Right username!")
                    pause_long()
                else:
                    print("❌ Username is not right!")
                    pause_long()
                    continue
                password_to_log_in = input("⌨️  Enter password of account to log in: ").strip()
                pause_long()
                if password_to_log_in == account["Password"]:
                    print("✅ Right password!")
                    pause_long()
                else:
                    print("❌ Password is not right!")
                    pause_long()
                    continue  
                print(f"✅ You log in to account {account["Username"]}!")                 
                log_in_to_account = True
                return log_in_to_account
            else:
                print("❗ You already log in to account!")
                pause_long()
                return log_in_to_account
        else:
            print("❗ You don't create account to log in!")
            pause_long()
            return log_in_to_account

def log_out(account:dict, log_in_to_account:bool):
    while True:
        if not log_in_to_account:
            print("❗ You need firstly log in to account before log out!")
            pause_long()
            return log_in_to_account
        else:
            sure_to_log_out = input("⌨️  Are you sure to log out? (Enter yes/no)").strip()
            pause_long()
            if sure_to_log_out == "yes":
                print("⚙️ Log out started!")
                pause_long()
                log_in_to_account = False
                print("❗ You are log out from account!")
                pause_long()
                return log_in_to_account
            elif sure_to_log_out == "no":
                print("❗ Exit log out!")
                pause_long()
                return log_in_to_account
            else:
                print("❗ Enter yes or no!")
                pause_long()
                continue

def exit_program(account):
    print("🪪 Your account:")
    pause_long()
    for key, value in account.items():
        print(f"• {key}: {value}")
        pause_short()
    pause_long()
    print("👋 Goodbye!")
    pause_long()

while True:
    menu()
    try:
        user_choice = int(input("⌨️  Enter your choice:"))
        pause_long()
        if user_choice == 1:
            account, have_account = registration_account(account, have_account)
        elif user_choice == 2:
            log_in_to_account = log_in(account, log_in_to_account)
        elif user_choice == 3:
            log_in_to_account = log_out(account, log_in_to_account)
        elif user_choice == 4:
            exit_program(account)
            break
        else:
            print("❗ Enter right number!")
            pause_long()
            continue
    except ValueError:
        pause_long()
        print("❗ Enter number!")
        pause_long()
        continue 
    