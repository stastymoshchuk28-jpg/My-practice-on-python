from time import sleep
#Not done
#v0.1

books = set()
start = True

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def menu(start):
    print("=== 📚 Library Inventory Manager ===")
    oformity1()
    if start:
        print("👋 Welcome! Let's manage your library.")
        oformity1()
        start = False
    print("⌨️  Choose what to do:")
    oformity1()
    print("1️⃣  1. Add a book")
    oformity2()
    print("2️⃣  2. Check out a book")
    oformity2()
    print("3️⃣  3. Return a book")
    oformity2()
    print("4️⃣  4. Show all books")
    oformity2()
    print("5️⃣  5. Show unique genres")
    oformity2()
    print("6️⃣  6. Search for a book")
    oformity2()
    print("7️⃣  7. Exit")
    oformity1()
    return start



while True:
    start = menu(start)
    try:
        user_choice = int(input("⌨️  Enter your choice: "))
        oformity1()
    except ValueError:
        oformity1()
        print("❗ Please enter a number, not text!")
        oformity1()
        continue
    if user_choice < 1:
        print("❗ Choice need to be bigger than 1!")
        oformity1()
        continue
    elif user_choice > 7:
        print("❗ Choice is too big!")
        oformity1()
        continue

    if user_choice == 1:
        ...
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
    elif user_choice == 7:
        ...