from time import sleep
#Not done
#v0.1

books = {}
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

def add_book(books:dict):
    while True:
        in_books = False

        book_title = input("⌨️  Enter the book title: ").strip()
        oformity1()

        for k in books.keys():
            k = k.lower()
            b = book_title.lower()
            if k == b:
                in_books = True
                break

        book_author = input("⌨️  Enter the author: ").strip()
        oformity1()
    
        book_genre = input("⌨️  Enter the genre: ").strip()
        oformity1()

        try:
            book_copies = int(input("⌨️  How many copies? "))    
            oformity1()
        except ValueError:
            oformity1()
            print("❗ Please, enter number!")
            oformity1()
            continue

        if in_books:
            print("📕 This book already exists - added more copies instead.")
            added_copy = False
            for k, v in books.items():
                for valye in v.values():
                    if valye == book_author:
                        books[k]["copies"] += 1
                        added_copy = True
                        break
                    elif valye == book_genre:
                        books[k]["copies"] += 1
                        added_copy = True
                        break
                    else:
                        continue
                if k == book_title:
                    books[k]["copies"] += 1
                    added_copy = True
                if added_copy:
                    break
            return books
        else:
            book_to_add = {"author": book_author, "genre": book_genre, "copies": book_copies}
            books[book_title] = book_to_add
            return books

while True:
    start = menu(start)
    print(books)
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
        add_book(books)
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