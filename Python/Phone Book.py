from time import sleep

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
            text = text + f"Name: {contact_name} \n Number: {contact_number};\n"
        text = text[0: -2: 1]
        print(text)
        oformity1()

def add_contact(contacts):
    while True:
        user_new_contact_name = input("⌨️  Write name of contact: ").strip()
        if not user_new_contact_name == "":
            oformity2()
            user_new_contact_number = input("⌨️  Write number of contact: ").strip().capitalize()
            oformity1()
            if not user_new_contact_number == "":
                lenght_letters = len(user_new_contact_number)
                right_letters = 0
                numbers = 0
                pluses = 0
                can_be_number = False
                for let in user_new_contact_number:
                    if not let.isdigit() and not let == "+" and not let == " ":
                        continue
                    else:
                        if let == "+":
                            pluses += 1
                        elif let.isdigit():
                            numbers += 1
                        right_letters += 1
                        continue
                if right_letters == lenght_letters:
                    if numbers > 1:
                        if pluses == 1:
                            can_be_number = True
                else:
                    if numbers == 0:
                        if pluses == 0 or pluses > 1:
                            can_be_number = False
                if can_be_number:
                    contact_in_contacts = False
                    for contact in contacts:
                        contact_name = contact[0]
                        contact_number = contact[1]
                        if user_new_contact_name == contact_name or user_new_contact_number == contact_number:
                            contact_in_contacts = True
                            break
                        else:
                            contact_in_contacts = False
                            continue
                    if contact_in_contacts:
                        print("❗ Contact already in contacts!")
                        oformity1()
                        continue
                    else:
                        contact_new = [user_new_contact_name, user_new_contact_number]
                        contacts.append(contact_new)
                        print("➕ Contact added to contacts!")
                        oformity1()
                        return contacts
            else:
                continue
        else:
            oformity1()
            continue

def delete_contact(contacts):
    if not contacts:
        print("❗ Don't found contact!")
        oformity1()
        return contacts
    
    def find_name(contacts, delete_name):
        in_contacts = False
        name_contact = "No name"
        delete_index = "No index"
        for contact in contacts:
            delete_index = contacts.index(contact)
            name_contact = contact[0]
            if delete_name == name_contact:
                in_contacts = True
                break
            else:
                in_contacts = False
        return delete_index, name_contact, in_contacts

    def find_number(contacts, delete_number):
        in_contacts = False
        number_contact = "No number"
        delete_index = "No index"
        for contact in contacts:
            delete_index = contacts.index(contact)
            number_contact = contact[1]
            if delete_number == number_contact:
                in_contacts = True
                break
            else:
                in_contacts = False
        return delete_index, number_contact, in_contacts

    while True:
        print("=== Delete contact ===")
        oformity1()
        print("1️⃣  1. Delete by name")
        oformity2()
        print("2️⃣  2. Delete by number")
        oformity1()
        delete_choice = input("⌨️  Enter number of choice: ").strip()
        oformity1()
        if delete_choice.isdigit():
            delete_choice = int(delete_choice)
            if delete_choice == 1:
                names = ""
                for contact in contacts:
                    name = contact[0]
                    names = names + name + "; "
                names = names[0: -2: 1]
                print(f"📋 Names of contacts: {names}")
                oformity1()
                delete_name = input("⌨️  Enter name of contact to delete it:").strip()
                oformity1()
                delete_index, name_contact, in_contacts = find_name(contacts, delete_name)
                if in_contacts:
                    print(f"🗑️  {name_contact} deleted!")
                    contacts.pop(delete_index)
                    oformity1()
                    return contacts
                else:
                    print(f"❗ {name_contact} not found!")
                    oformity1()
                    return contacts
            elif delete_choice == 2:
                numbers = ""
                for contact in contacts:
                    number = contact[1]
                    numbers = numbers + number + "; "
                numbers = numbers[0: -2: 1]
                print(f"📋 Numbers of contacts: {numbers}")
                oformity1()
                delete_number = input("⌨️  Enter numbers of contact to delete it:").strip().capitalize()
                oformity1()
                delete_index, number_contact, in_contacts = find_number(contacts, delete_number)
                if in_contacts:
                    print(f"🗑️  {number_contact} deleted!")
                    contacts.pop(delete_index)
                    oformity1()
                    return contacts
                else:
                    print(f"❗ {number_contact} not found!")
                    oformity1()
                    return contacts
            else:
                print("❗ Not right number of choice!")
                oformity1()
                continue        
        elif delete_choice == "":
            print("❗ Choice can't be empty!")
            oformity1()
            continue
        else:
            print("❗ Choice need to be number!")
            oformity1()
            continue

def find_contact(contacts):
    def find_contact_by_name(contacts, name_to_find):
        contact_not_in_contacts = True
        for contact in contacts:
            contact_name = contact[0]
            if name_to_find == contact_name:
                contact_not_in_contacts = False
                return contact, contact_not_in_contacts
            else:
                contact_not_in_contacts = True
                continue
        return contact, contact_not_in_contacts

    while True:
        name_of_contact = input("⌨️  Enter name of contact to find it: ").strip()
        oformity1()
        if name_of_contact != "":
            contact, contact_not_in_contacts = find_contact_by_name(contacts, name_of_contact)
            if not contact:
                print("❗ Contact not found!")
                oformity1()
                continue
            if contact_not_in_contacts:
                print("❗ Contact not found!")
                oformity1()
                continue
            else:
                print("📱 Contact:")
                oformity1()
                print(f"👨 Name: {contact[0]}")
                oformity2()
                print(f"📱 Number: {contact[1]}")
                oformity1()
                break
        else:
            print("❗ Name of contact can't be empty!")
            oformity1()
            continue

def sort_contact(contacts):
    ...

def exit_proggram(contacts):
    show_contacts(contacts)
    print("👋 Goodbye!")
    oformity1()
    exit()

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
            contacts = add_contact(contacts)
        elif user_choice == 3:
            contacts = delete_contact(contacts)
        elif user_choice == 4:
            find_contact(contacts)
        elif user_choice == 5:
            ...
        elif user_choice == 6:
            exit_proggram(contacts)
        else:
            print("❗ Not right number of choice!")
            oformity1()
            continue
    elif user_choice == "":
        print("❗ Choice can't be empty!")
        oformity1()
        continue
    else:
        print("❗ Choice need to be number!")
        oformity1()
        continue