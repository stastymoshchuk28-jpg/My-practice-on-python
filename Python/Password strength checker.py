print("Welcome to the Password Strength Checker!")
print("Let's see how strong your password is.")
print("-------------------------------")
password = input("Enter a password: ")
print("-------------------------------")
print("🔍 Analyzing password...")
print("🔍 Checking password strength...")
print("-------------------------------")
if len(password) < 8:
    print("Password is too short. That's not good!")
    print("-------------------------------")
    if password != password.lower():
        print("Has uppercase letters. That's good!")
        print("-------------------------------")
        if password[0:8:1] == "password":
            print("Password contains 'password'. That's not good!")
            print("-------------------------------")
        else:
            print("Password does not contain 'password'. That's good!")
            print("-------------------------------")
    elif password == password.lower():
        print("No uppercase letters. That's not good!")
        print("-------------------------------")
        if password[0:8:1] == "password":
            print("Password contains 'password'. That's not good!")
            print("-------------------------------")
        else:
            print("Password does not contain 'password'. That's good!")
            print("-------------------------------")
elif len(password) >= 8:
    print("Password length is good.")
    print("-------------------------------")
    if password != password.lower():
        print("Has uppercase letters. That's good!")
        print("-------------------------------")
        if password[0:8:1] == "password":
            print("Password contains 'password'. That's not good!")
            print("-------------------------------")
        else:
            print("Password does not contain 'password'. That's good!")
            print("-------------------------------")
    elif password == password.lower():
        print("No uppercase letters. That's not good!")
        print("-------------------------------")
        if password[0:8:1] == "password":
            print("Password contains 'password'. That's not good!")
            print("-------------------------------")
        else:
            print("Password does not contain 'password'. That's good!")
            print("-------------------------------")