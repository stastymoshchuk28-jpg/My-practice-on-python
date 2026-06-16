import time

symbol = ""
simbols = ""

print("Welcome to the comment writing!")
print(" ")
name = input("Write you name for comment: ")
print(" ")
comment = input("Enter your comment: ")
print(" ")
print("Thank's for comment!")
time.sleep(0.5)
print(" ")
print("Now AI agent will check it!")
time.sleep(0.5)
print(" ")
print("🔍Checking comment...")
print(" ")
time.sleep(2.5)

for char in comment:
    if char in "@#$":
        symbol = symbol + char + " ,"
        symbol = symbol[0: -3: 1]
        print(f"Sorry, your comment contains a prohibited symbol-(s): {symbol}!")
        exit()
print("No prohibited symbols, that's good!")
print(" ")
time.sleep(1.5)
for sym in comment:
    if ((sym != " " and sym != ".") and (sym != "!" and sym != ",")) and sym != "?":
        simbols = simbols + sym
if len(simbols) >= 350:
    print("Sorry, we are have limit of characters - 350!")
    exit()
else:
    print("Good, not in limit of characters!")
    print(" ")
print("🔍Thinking last time before publish comment...")
time.sleep(1.5)
print(" ")
print("Comment published!")
print(f"{name}: {comment}")