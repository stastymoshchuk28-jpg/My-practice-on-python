#done!

import time

print("Welcome to the Password Strength Checker!")
print("Let's see how strong your password is.")
print("-------------------------------")
password = input("Enter a password: ")
strength = 0
print("-------------------------------")
print("🔍 Analyzing password...")
time.sleep(1)
print("🔍 Checking password strength...")
time.sleep(1)
print("-------------------------------")
if len(password) < 8:
    print("❗Password is too short!")
    print("-------------------------------")
    time.sleep(1)
    for let in password:
        if let.isdigit():
            print("✅ Contains numbers.")
            print("-------------------------------")
            time.sleep(1)
            strength += 1
            break
    for let in password:
        if let.isupper():
            print("✅ Contains uppercase letters.")
            print("-------------------------------")
            time.sleep(1)
            strength += 1
            break
    for let in password:
        if let.islower():
            print("✅ Contains lowercase letters.")
            print("-------------------------------")
            time.sleep(1)
            strength += 1
            break
    if strength == 0:
        print("❗Password is very weak!")
    elif strength == 1:
        print("⚠️ Password is weak!")
    elif strength == 2:
        print("⚠️ Password is moderate!")
    else:
        print("✅ Password is strong!")
elif len(password) >= 8:
    print("✅Password length is good.")
    print("-------------------------------")
    strength += 1
    time.sleep(1)
    for let in password:
        if let.isdigit():
            print("✅ Contains numbers.")
            print("-------------------------------")
            time.sleep(1)
            strength += 1
            break
    for let in password:
        if let.isupper():
            print("✅ Contains uppercase letters.")
            print("-------------------------------")
            time.sleep(1)
            strength += 1
            break
    for let in password:
        if let.islower():
            print("✅ Contains lowercase letters.")
            print("-------------------------------")
            time.sleep(1)
            strength += 1
            break
    if strength == 0:
        print("❗Password is very weak!")
    elif strength == 1:
        print("⚠️ Password is weak!")
    elif strength == 2:
        print("⚠️ Password is moderate!")
    else:
        print("✅ Password is strong!")