print("Welcome!")
print(" ")
name = input("Please, write your name: ").capitalize()
print(" ")
print(f"How many tickets you want buy, {name}?")
print(" ")
tickets_left = 5
tickets_buyed = 0
while tickets_left > 0:
    print(f"We are left {tickets_left} tickets!")
    print(" ")
    want_buy = input("Please write number of tickets to buy or 'exit' to end buying: ")
    print(" ")
    if want_buy == "exit":
        break
    elif want_buy.isdigit():
        want_buy_new = int(want_buy)
        if want_buy_new > tickets_left:
            print(f"We are have only {tickets_left}!")
            print(" ")
            continue
        else:
            tickets_left -= want_buy_new
            tickets_buyed += want_buy_new
            print(f"You are bought {want_buy_new} tickets!")
            print(" ")
            print(f"You can buy {tickets_left} more tickets!")
print(f"Thank's for buying, {name}!")
print(" ")
print(f"You are bought {tickets_buyed}!")