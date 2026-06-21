user_balance = 500 #Variables
spent = 0
apple_cost = 2
headphones_cost = 150
t_shirt_cost = 40
book_cost = 15
buying = ""

print("=== Welcome to PyShop ===")
print("Your balance: $500")
print(" ")
print("You can choose from:")
print(f"1. Apple - ${apple_cost}")
print(f"2. Headphones - ${headphones_cost}")
print(f"3. T-shirt - ${t_shirt_cost}")
print(f"4. Book - ${book_cost}")
print(f"5. Exit online shop")
print(" ")
while True:
    user_choice = int(input("Choose number of item: "))
    if user_balance > 0:
        if user_choice == 1:
            print(f"You bought apple for ${apple_cost}")
            buying = buying + "Apple, "
            user_balance -= apple_cost
            print(f"Balance left: {user_balance}")
            print(" ")
            continue
        elif user_choice == 2:
            print(f"You bought headphones for ${headphones_cost}")
            buying = buying + "Headphones, "
            user_balance -= headphones_cost
            print(f"Balance left: {user_balance}")
            print(" ")
            continue
        elif user_choice == 3:
            print(f"You bought t-shirt for ${t_shirt_cost}")
            buying = buying + "T-shirt, "
            user_balance -= t_shirt_cost
            print(f"Balance left: {user_balance}")
            print(" ")
            continue
        elif user_choice == 4:
            print(f"Yoy bought book for ${book_cost}")
            buying = buying + "Book, "
            user_balance -= book_cost
            print(f"Balance left: {user_balance}")
            print(" ")
            continue
        elif user_choice == 5:
            spent = 500 - user_balance
            buying = buying[0: -2: 1]
            print(" ")
            print("=== Receipt ===")
            print(f"You buyed - {buying}")
            print(f"Total spent - {spent}")
            print(f"Balance left - {user_balance}")
            print("Thanks for buying at our shop!")
            break
