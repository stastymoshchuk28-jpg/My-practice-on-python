from time import sleep
#Done
#v1.0

books = {}
picked_books = {}
start = True

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)

def menu(start):
    print("=== 📚 Library Inventory Manager ===")
    pause_long()
    if start:
        print("👋 Welcome! Let's manage your library.")
        pause_long()
        start = False
    print("⌨️  Choose what to do:")
    pause_long()
    print("1️⃣  1. Add a book")
    pause_short()
    print("2️⃣  2. Check out a book")
    pause_short()
    print("3️⃣  3. Return a book")
    pause_short()
    print("4️⃣  4. Show all books")
    pause_short()
    print("5️⃣  5. Show unique genres")
    pause_short()
    print("6️⃣  6. Search for a book")
    pause_short()
    print("7️⃣  7. Exit")
    pause_long()
    return start

def add_book(books:dict):
    while True:
        in_books = False

        book_title = input("⌨️  Enter the book title: ").strip()
        pause_long()

        for k in books.keys():
            k = k.lower()
            b = book_title.lower()
            if k == b:
                in_books = True
                break

        book_author = input("⌨️  Enter the author: ").strip()
        pause_long()
    
        book_genre = input("⌨️  Enter the genre: ").strip()
        pause_long()

        try:
            book_copies = int(input("⌨️  How many copies? "))    
            pause_long()
        except ValueError:
            pause_long()
            print("❗ Please, enter number!")
            pause_long()
            continue

        if in_books:
            print(f"📕 This book already exists - added more copies instead (You write to add: {book_copies}).")
            added_copy = False
            for k in books.keys():
                if added_copy:
                    break
                if k == book_title.lower():
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
        pause_long()
        return books, picked_books
    while True:
        book_to_out = input("⌨️  Enter the title of the book to check out: ").strip()
        pause_long()

        check_book = False
        for k in books.keys():
            if book_to_out.lower() == k.lower():
                check_book = book_to_out
                book_to_out = k
                break
        
        if not check_book:
            print("❗ Sorry, this book is not in the library!")
            pause_long()
            continue
        else:
            book_info = books[book_to_out]
            if book_info["copies"] <= 0:
                print("❗ Sorry, all copies are currently checked out!")
                pause_long()
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
                pause_long()
                break
    return books, picked_books

def return_book(books:dict, picked_books:dict):
    if not books:
        print("❗ Your library is empty!")
        pause_long()
        return books, picked_books
    if not picked_books:
        print("❗ You don't check out any book to return!")
        pause_long()
        return books, picked_books
    while True:
        book_to_return = input("⌨️  Enter the title of the book to return: ").strip()
        pause_long()

        check_book1 = False
        check_book2 = False
        for k in books.keys():
            if k.lower() == book_to_return.lower():
                book_to_return = k
                check_book1 = book_to_return
                break
        for k in picked_books.keys():
            if k.lower() == book_to_return.lower():
                check_book2 = book_to_return
                break
        
        
        if not check_book1:
            print("❗ This book wasn't checked out!")
            pause_long()
            continue
        else:
            if not check_book2:
                print("❗ This book doesn't belong to our library.")
                pause_long()
                continue
            else:
                book_info = picked_books[book_to_return]
                if book_info["copies"] <= 0:
                    print("❗ Sorry, all copies are currently return!")
                    pause_long()
                    break
                else:
                    book_info["copies"] -= 1
                    print(f"📕 Return successfully! Copies left (of check out books): {book_info["copies"]}")
                    picked_books[book_to_return]["copies"] -= 1
                    books[book_to_return]["copies"] += 1
                    if picked_books[book_to_return]["copies"] <= 0:
                        picked_books.pop(book_to_return, False)
                    pause_long()
                    break
    return books, picked_books    

def show_all_books(books:dict):
    if not books:
        print("❗ Your library is empty!")
        pause_long()
    else:
        print("=== 📖 All Books ===")
        pause_long()
        for name, info in books.items():
            author_of_book = info["author"]
            genre_of_book = info["genre"]
            copies_of_book = info["copies"]
            print(f"📕 Title: {name}")
            print(f"👨 Author: {author_of_book}")
            print(f"⚙️  Genre: {genre_of_book}")
            print(f"📚 Copies: {copies_of_book}")
            pause_short()
        pause_long()

def show_unique_genres(books:dict):
    if not books:
        print("❗ Your library is empty!")
        pause_long()
    else:
        print("=== 🏷️ Unique Genres in the Library ===")
        unique_genres = set()
        for info_of_book in books.values():
            gen = info_of_book["genre"]
            unique_genres.add(gen)
        text = ""
        for g in unique_genres:
            text = text + f"{g}; "
        print(f"⚙️✨ Total unique genres: {text}")
        pause_long()

def search_for_book(books:dict):
    if not books:
        print("❗ Your library is empty!")
        pause_long()
    else:
        book_to_search = input("⌨️  Enter a title to search: ").strip()
        pause_long()

        book_found = False
        for k in books.keys():
            if k.lower() == book_to_search.lower():
                book_to_search = k
                book_found = True
                break

        if book_found:
            print(f"🔍 {book_to_search} found!")
            pause_long()
            info_of_book = books[book_to_search]
            print("🪪  Info about book:")
            pause_long()
            print(f"📕 Title: {book_to_search}")
            pause_short()
            print(f"👨 Author: {info_of_book["author"]}")
            pause_short()
            print(f"⚙️  Genre: {info_of_book["genre"]}")
            pause_short()
            print(f"📚 Copies: {info_of_book["copies"]}")
            pause_long()
        else:
            print(f"❌ {book_to_search} not found!")
            pause_long()

def exit_proggram(books:dict):
    print("📚 Thank you for using Library Inventory Manager!")
    pause_long()
    show_all_books(books)
    print("👋 Goodbye!")

while True:
    start = menu(start)
    try:
        user_choice = int(input("⌨️  Enter your choice: "))
        pause_long()
    except ValueError:
        pause_long()
        print("❗ Please enter a number, not text!")
        pause_long()
        continue
    if user_choice < 1:
        print("❗ Choice need to be bigger than 1!")
        pause_long()
        continue
    elif user_choice > 7:
        print("❗ Choice is too big!")
        pause_long()
        continue

    if user_choice == 1:
        books = add_book(books)
    elif user_choice == 2:
        books, picked_books = check_out_book(books, picked_books)
    elif user_choice == 3:
        books, picked_books = return_book(books, picked_books)
    elif user_choice == 4:
        show_all_books(books)
    elif user_choice == 5:
        show_unique_genres(books)
    elif user_choice == 6:
        search_for_book(books)
    elif user_choice == 7:
        exit_proggram(books)
        break
    else:
        print("❗ Not right choice!")
        continue