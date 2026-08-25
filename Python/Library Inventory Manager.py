from time import sleep
#Not done
#v0.1

books = {}
picked_books = {}
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
            print(f"📕 This book already exists - added more copies instead (You write to add: {book_copies}).")
            added_copy = False
            for k in books.keys():
                if added_copy:
                    break
                if k == book_title:
                    books[k]["copies"] += book_copies
                    added_copy = True
            return books
        else:
            book_to_add = {"author": book_author, "genre": book_genre, "copies": book_copies}
            books[book_title] = book_to_add
            return books

def check_out_book(books:dict, picked_books:dict):
    if not books:
        print("❗ Your library is empty! Can't check out from empty library!")
        oformity1()
        return books, picked_books
    while True:
        book_to_out = input("⌨️  Enter the title of the book to check out: ").strip()
        oformity1()

        check_book = books.get(book_to_out, False)
        if not check_book:
            print("❗ Sorry, this book is not in the library!")
            oformity1()
            continue
        else:
            book_info = books[book_to_out]
            if book_info["copies"] <= 0:
                print("❗ Sorry, all copies are currently checked out!")
                oformity1()
                break
            else:
                book_info["copies"] -= 1
                print(f"📕 Checked out successfully! Copies left: {book_info["copies"]}")
                if book_to_out in picked_books:
                    picked_books[book_to_out]["copies"] += 1
                else:
                    book_info_for_out = book_info.copy()
                    book_info_for_out["copies"] = 1
                    picked_books[book_to_out] = book_info_for_out
                oformity1()
                break
    return books, picked_books

def return_book(books:dict, picked_books:dict):
    if not books:
        print("❗ Your library is empty!")
        oformity1()
        return books, picked_books
    if not picked_books:
        print("❗ You don't check out any book to return!")
        oformity1()
        return books, picked_books
    while True:
        book_to_return = input("⌨️  Enter the title of the book to return: ").strip()
        oformity1()

        check_book1 = picked_books.get(book_to_return, False)
        check_book2 = books.get(book_to_return, False)
        if not check_book1:
            print("❗ This book wasn't checked out!")
            oformity1()
            continue
        else:
            if not check_book2:
                print("This book doesn't belong to our library.")
            if book_to_return in picked_books:
                book_info = picked_books[book_to_return]
            else:
                print("❗ This book doesn't checked out!")
            if book_info["copies"] <= 0:
                print("❗ Sorry, all copies are currently return!")
                oformity1()
                break
            else:
                book_info["copies"] -= 1
                print(f"📕 Return successfully! Copies left: {book_info["copies"]}")
                picked_books[book_to_return]["copies"] -= 1
                if picked_books[book_to_return]["copies"] <= 0:
                    found_book = picked_books.pop(book_to_return, False)
                oformity1()
                break
    return books, picked_books    

def show_all_books(books:dict):
    if not books:
        print("❗ Your library is empty!")
        oformity1()
    else:
        print("=== 📖 All Books ===")
        oformity1()
        for name, info in books.items():
            aut = info["author"]
            gen = info["genre"]
            cop = info["copies"]
            print(f"📕 Title: {name}")
            print(f"👨 Author: {aut}")
            print(f"⚙️ Genre: {gen}")
            print(f"📚 Copies: {cop}")
            oformity2()

def show_unique_genres(books:dict):
    if not books:
        print("❗ Your library is empty!")
        oformity1()
    else:
        unique_genres = set()
        for info_of_book in books.values():
            gen = info_of_book["genre"]
            unique_genres.add(gen)
        print(f"⚙️✨ Unique genres: {unique_genres}")
        oformity1()

def search_for_book(books):
    if not books:
        print("❗ Your library is empty!")
        oformity1()
    else:
        book_to_search = input("⌨️  Enter name of book to search it: ").strip()
        oformity1()

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
        books = add_book(books)
    elif user_choice == 2:
        books, picked_books = check_out_book(books, picked_books)
    elif user_choice == 3:
        return_book(books, picked_books)
    elif user_choice == 4:
        show_all_books(books)
    elif user_choice == 5:
        show_unique_genres(books)
    elif user_choice == 6:
        ...
    elif user_choice == 7:
        ...
    else:
        print("❗ Not right choice!")
        continue