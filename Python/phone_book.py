#Done!
#v1.0

from time import sleep

contacts = []

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)

def show_contacts(contacts):
    if not contacts:
        print("❗ Contacts empty!")
        pause_long()
    else:
        print("📱 Your contacts: ")
        text = ""
        for contact in contacts:
            contact_name = contact[0]
            contact_number = contact[1]
            text = text + f"Name: {contact_name}\n Number: {contact_number};\n"
        text = text[0: -2: 1]
        print(text)
        pause_long()

def add_contact(contacts):
    while True:
        user_new_contact_name = input("⌨️  Write name of contact: ").strip()
        if not user_new_contact_name == "":
            pause_short()
            user_new_contact_number = input("⌨️  Write number of contact: ").strip().capitalize()
            pause_long()
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
                        pause_long()
                        continue
                    else:
                        contact_new = [user_new_contact_name, user_new_contact_number]
                        contacts.append(contact_new)
                        print("➕ Contact added to contacts!")
                        pause_long()
                        return contacts
            else:
                continue
        else:
            pause_long()
            continue

def delete_contact(contacts):
    if not contacts:
        print("❗ Don't found contact!")
        pause_long()
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
        pause_long()
        print("1️⃣  1. Delete by name")
        pause_short()
        print("2️⃣  2. Delete by number")
        pause_long()
        delete_choice = input("⌨️  Enter number of choice: ").strip()
        pause_long()
        if delete_choice.isdigit():
            delete_choice = int(delete_choice)
            if delete_choice == 1:
                names = ""
                for contact in contacts:
                    name = contact[0]
                    names = names + name + "; "
                names = names[0: -2: 1]
                print(f"📋 Names of contacts: {names}")
                pause_long()
                delete_name = input("⌨️  Enter name of contact to delete it:").strip()
                pause_long()
                delete_index, name_contact, in_contacts = find_name(contacts, delete_name)
                if in_contacts:
                    print(f"🗑️  {name_contact} deleted!")
                    contacts.pop(delete_index)
                    pause_long()
                    return contacts
                else:
                    print(f"❗ {name_contact} not found!")
                    pause_long()
                    return contacts
            elif delete_choice == 2:
                numbers = ""
                for contact in contacts:
                    number = contact[1]
                    numbers = numbers + number + "; "
                numbers = numbers[0: -2: 1]
                print(f"📋 Numbers of contacts: {numbers}")
                pause_long()
                delete_number = input("⌨️  Enter numbers of contact to delete it:").strip().capitalize()
                pause_long()
                delete_index, number_contact, in_contacts = find_number(contacts, delete_number)
                if in_contacts:
                    print(f"🗑️  {number_contact} deleted!")
                    contacts.pop(delete_index)
                    pause_long()
                    return contacts
                else:
                    print(f"❗ {number_contact} not found!")
                    pause_long()
                    return contacts
            else:
                print("❗ Not right number of choice!")
                pause_long()
                continue        
        elif delete_choice == "":
            print("❗ Choice can't be empty!")
            pause_long()
            continue
        else:
            print("❗ Choice need to be number!")
            pause_long()
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
        pause_long()
        if name_of_contact != "":
            contact, contact_not_in_contacts = find_contact_by_name(contacts, name_of_contact)
            if not contact:
                print("❗ Contact not found!")
                pause_long()
                continue
            if contact_not_in_contacts:
                print("❗ Contact not found!")
                pause_long()
                continue
            else:
                print("📱 Contact:")
                pause_long()
                print(f"👨 Name: {contact[0]}")
                pause_short()
                print(f"📱 Number: {contact[1]}")
                pause_long()
                break
        else:
            print("❗ Name of contact can't be empty!")
            pause_long()
            continue

def sort_contact(contacts):
    if not contacts:
        print("❗ Contacts empty, can't sort!")
        pause_long()
    else:
        while True:
            print("=== Sort contacts ===")
            pause_long()
            print("1️⃣  1. Sort by name")
            print("2️⃣  2. Sort by number")
            pause_long()
            user_choice = input("⌨️  Enter your choice: ").strip()
            if user_choice.isdigit():
                user_choice = int(user_choice)
                if user_choice == 1:
                    contacts.sort(key = lambda contact: contact[0])
                    text = ""
                    for contact in contacts:
                        text = text + f"Name: {contact[0]}\nNumber: {contact[1]};\n"
                    text = text[0: -2: 1]
                    print(f"📱 Sorted Contacts:\n {text}")
                    pause_long()
                    return contacts
                elif user_choice == 2:
                    contacts.sort(key = lambda contact: contact[1])
                    text = ""
                    for contact in contacts:
                        text = text + f"Name: {contact[0]}\nNumber: {contact[1]};\n"
                    text = text[0: -2: 1]
                    print(f"📱 Sorted Contacts:\n {text}")
                    pause_long()
                    return contacts
                else:
                    print("❗ Not right number of choice!")
                    pause_long()
                    continue
            elif user_choice == "":
                print("❗ Choice can't be empty!")
                pause_long()
                continue
            else:
                print("❗ Choice need to be number!")
                pause_long()
                continue

def exit_proggram(contacts):
    show_contacts(contacts)
    print("👋 Goodbye!")
    pause_long()
    exit()

while True:
    print("=== Phone Book ===")
    pause_long()
    print("1️⃣  1. Show contacts")
    pause_short()
    print("2️⃣  2. Add contact")
    pause_short()
    print("3️⃣  3. Delete contact")
    pause_short()
    print("4️⃣  4. Find contact")  
    pause_short()
    print("5️⃣  5. Sort contacts")
    pause_short()
    print("6️⃣  6. Exit")
    pause_long()
    user_choice = input("⌨️  Enter your choice: ").strip()
    pause_long()
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
            contacts = sort_contact(contacts)
        elif user_choice == 6:
            exit_proggram(contacts)
        else:
            print("❗ Not right number of choice!")
            pause_long()
            continue
    elif user_choice == "":
        print("❗ Choice can't be empty!")
        pause_long()
        continue
    else:
        print("❗ Choice need to be number!")
        pause_long()
        continue