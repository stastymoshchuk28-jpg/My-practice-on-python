#done!
#v1.0
from time import sleep

account = {
    "Username": None,
    "Password": None,
}

have_account = False
log_in_to_account = False

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def menu():
    print("=== Registration System ===")
    oformity1()
    print("1️⃣  Create account")
    oformity2()
    print("2️⃣  Log in to account")
    oformity2()
    print("3️⃣  Log out from account")
    oformity2()
    print("4️⃣  Exit")
    oformity1()

def registration_account(account:dict, have_account:bool):
    while True:
        if not have_account:
            user_name = input("⌨️  Enter username for account: ").strip()
            oformity1()
            if user_name == "":
                print("❗ Username can't be empty!")
                oformity1()
                continue
            elif user_name.isdigit():
                print("❗ Username can't be just numbers!")
                oformity1()
                continue
            else:
                print("✅ Username saved!")
                oformity1()
            password = input("⌨️  Enter password for account: ").strip()
            if password == "":
                print("❗ Password can't be empty!")
                oformity1()
                continue
            elif password.isdigit():
                print("❗ Password can't be just numbers!")
                oformity1()
                continue
            else:
                print("✅ Password saved!")
                oformity1()
            account.update(Username=user_name, Password=password)
            have_account = True
            print("✅ Account created!")
            oformity1()
            return account, have_account
        else:
            print("❗ You already have account!")
            oformity1()
            return account, have_account
        
def log_in(account:dict, log_in_to_account:bool):
    while True:
        if account["Username"] != None and account["Password"] != None:
            if log_in_to_account == False:
                print("⚙️ Log in to account:")
                oformity1()
                user_name_to_log_in = input("⌨️  Enter username of account to log in: ").strip()
                oformity1()
                if user_name_to_log_in == account["Username"]:
                    print("✅ Right username!")
                    oformity1()
                else:
                    print("❌ Username is not right!")
                    oformity1()
                    continue
                password_to_log_in = input("⌨️  Enter password of account to log in: ").strip()
                oformity1()
                if password_to_log_in == account["Password"]:
                    print("✅ Right password!")
                    oformity1()
                else:
                    print("❌ Password is not right!")
                    oformity1()
                    continue  
                print(f"✅ You log in to account {account["Username"]}!")                 
                log_in_to_account = True
                return log_in_to_account
            else:
                print("❗ You already log in to account!")
                oformity1()
                return log_in_to_account
        else:
            print("❗ You don't create account to log in!")
            oformity1()
            return log_in_to_account

def log_out(account:dict, log_in_to_account:bool):
    while True:
        if not log_in_to_account:
            print("❗ You need firstly log in to account before log out!")
            oformity1()
            return log_in_to_account
        else:
            sure_to_log_out = input("⌨️  Are you sure to log out? (Enter yes/no)").strip()
            oformity1()
            if sure_to_log_out == "yes":
                print("⚙️ Log out started!")
                oformity1()
                log_in_to_account = False
                print("❗ You are log out from account!")
                oformity1()
                return log_in_to_account
            elif sure_to_log_out == "no":
                print("❗ Exit log out!")
                oformity1()
                return log_in_to_account
            else:
                print("❗ Enter yes or no!")
                oformity1()
                continue

def exit_program(account):
    print("🪪 Your account:")
    oformity1()
    for key, value in account.items():
        print(f"• {key}: {value}")
        oformity2()
    oformity1()
    print("👋 Goodbye!")
    oformity1()

while True:
    menu()
    try:
        user_choice = int(input("⌨️  Enter your choice:"))
        oformity1()
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
            oformity1()
            continue
    except ValueError:
        oformity1()
        print("❗ Enter number!")
        oformity1()
        continue 
    