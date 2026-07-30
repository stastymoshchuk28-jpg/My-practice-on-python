from time import sleep()

contacts = []

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def show_contacts(contacts):
    if not contacts:
        print("❗ Contacts empty!")
        oformity1()
    else:
        print("📱 Your contacts: ")
        text = ""
        for contact in contacts:
            contact_name = contact[0]
            contact_number = contact[1]
            text = text + f"Name: {contact_name} \n Number: {contact_number}; \n"
        text = text[0: -2: 1]
        print(text)
        oformity1()

def add_contact(contacts):
    while True:
        user_new_contact_name = input("⌨️  Write name of contact: ").strip().capitalize()
        user_new_contact_number = input("⌨️  Write number of contact: ").strip().capitalize()
        lenght_letters = len(user_new_contact_number)
        right_letters = 0
        for let in user_new_contact_number:
            if not let.isdigit() and not let == "+" and not let == " ":
                continue
            else:
                right_letters += 1
                continue
        if right_letters == lenght_letters:
            can_be_number = True
        else:
            can_be_number = False
        if can_be_number:
            if not user_new_contact_name in contacts and not user_new_contact_name in 

while True:
    print("=== Phone Book ===")
    oformity1()
    print("1️⃣  1. Show contacts")
    oformity2()
    print("2️⃣  2. Add contact")
    oformity2()
    print("3️⃣  3. Delete contact")
    oformity2()
    print("4️⃣  4. Find contact")  
    oformity2()
    print("5️⃣  5. Sort contacts")
    oformity2()
    print("6️⃣  6. Exit")
    oformity1()
    user_choice = input("⌨️  Enter your choice: ").strip()
    oformity1()
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:
            show_contacts(contacts)
        elif user_choice == 2:
            ...
        elif user_choice == 3:
            ...
        elif user_choice == 4:
            ...
        elif user_choice == 5:
            ...
        elif user_choice == 6:
            ...
    elif user_choice == "":
        print("❗ Choice can't be empty!")
        oformity1()
        continue
    else:
        print("❗ Choice need to be number!")
        oformity1()
        continue