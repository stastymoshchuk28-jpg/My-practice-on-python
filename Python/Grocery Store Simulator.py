import time

breads, apples, milks, eggss, waters = 0, 0, 0, 0, 0
worth = 0.0

def buy_good():
    global breads, apples, milks, eggss, waters, worth
    goods = ["Bread", "Apple", "Milk", "Eggs", "Water"]
    prices = [2.5, 0.6, 3.0, 4.5, 1]

    time.sleep(0.5)
    print("❓ Choose what buy:")
    print(" ")
    it = 0
    p = 0.0
    for g in goods:
        if it == 0:
            p = 2.5
        elif it == 1:
            p = 0.6
        elif it == 2:
            p = 3.0
        elif it == 3:
            p = 4.5
        elif it == 4:
            p = 1
        print(f"🍴 Good: {g} | 💰 Price: {p}")
        print(" ")
        it += 1
        p = 0
        time.sleep(0.5)

    while True:
        buying_good = input("🍴 Enter name of good: ").capitalize()
        print(" ")
        time.sleep(1)
        if buying_good == "Bread":
            print("➕ You add bread to cart!")
            print(" ")
            time.sleep(1)
            breads += 1
            worth += prices[0]
            print(f"💰 Worth of purchase: {worth:.2f}")
            print(" ")
            time.sleep(1)
            break
        elif buying_good == "Apple":
            print("➕ You add apple to cart!")
            print(" ")
            time.sleep(1)
            apples += 1
            worth += prices[1]
            print(f"💰 Worth of purchase: {worth:.2f}")
            print(" ")
            time.sleep(1)
            break
        elif buying_good == "Milk":
            print("➕ You add milk to cart!")
            print(" ")
            time.sleep(1)
            milks += 1
            worth += prices[2]
            print(f"💰 Worth of purchase: {worth:.2f}")
            print(" ")
            time.sleep(1)
            break
        elif buying_good == "Eggs":
            print("➕ You add eggs to cart!")
            print(" ")
            time.sleep(1)
            eggss += 1
            worth += prices[3]
            print(f"💰 Worth of purchase: {worth:.2f}")
            print(" ")
            time.sleep(1)
            break
        elif buying_good == "Water":
            print("➕ You add water to cart!")
            print(" ")
            time.sleep(1)
            waters += 1
            worth += prices[4]
            print(f"💰 Worth of purchase: {worth:.2f}")
            print(" ")
            time.sleep(1)
            break
        else:
            print("❗ Not right name of the good!")
            print(" ")
            time.sleep(1)
            continue
    print("⏳ Please, wait...")
    time.sleep(5)

def at_cash_register(name):
    global worth, breads, apples, milks, eggss, waters

    print(f"✨ Thank you for buying goods at our store, {name}!")
    print(" ")
    print("=== ✨Stats of buying: ===")
    print(" ")
    if breads > 0:
        print(f"🥖 Breads: {breads}")
        print(" ")
        time.sleep(0.5)
    if apples > 0:
        print(f"🍎 Apples: {apples}")
        print(" ")
        time.sleep(0.5)
    if milks > 0:
        print(f"🥛 Milks: {milks}")
        print(" ")
        time.sleep(0.5)
    if eggss > 0:
        print(f"🥚 Eggs: {eggss}")
        print(" ")
        time.sleep(0.5)
    if waters > 0:
        print(f"🫗 Water: {waters}")
        print(" ")
        time.sleep(0.5)
    print(f"💰 Total cost of purchase: {worth:.2f}")
    print(" ")

print("=== 🛒 Grocery Store Simulator! ===")
print(" ")
time.sleep(0.5)
print("👋 Welcome to our grocery store 'Boberchik store'!")
print(" ")
time.sleep(0.5)
name = input("❓ Write your name: ")
print(" ")
time.sleep(0.5)
print("✨ Thanks! Now go choose what to buy and go to cash register with your goods!")
print(" ")
time.sleep(0.5)
while True:
    print("❓ Choose what to do:")
    print("1️⃣  1. Choose another good.")
    print("2️⃣  2. Go to the cash register and buy goods.")
    print(" ")
    time.sleep(0.5)
    choose = input("🔢 Write number of choice: ")
    print(" ")
    time.sleep(0.5)
    if choose.isalpha():
        print("❗ Choice can't be letter!")
        print(" ")
        continue
    elif choose.isdigit():
        choose = int(choose)
        if choose == 1:
            buy_good()
            time.sleep(0.5)
            continue
        elif choose == 2:
            at_cash_register(name)
            time.sleep(0.5)
            break
        else:
            print("❗ Not right number of choice!")
            print(" ")
            continue
    else:
        print("❗ Choice can't be letter!")
        print(" ")
        continue