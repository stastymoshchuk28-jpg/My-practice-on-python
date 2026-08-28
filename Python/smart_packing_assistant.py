#done!
#v1.0

import time

weather_items = []
base_items = []
activity_items = []
socks_and_underwear = 0

package_for_trip = [base_items, weather_items, activity_items, socks_and_underwear]

def info_of_trip():
    activityes = []
    swimming = False
    hiking = False
    business = False
    while True:
        weather = input("🌦️  What weather do you expect? (hot / cold / rainy) ").lower()
        print(" ")
        if weather != "hot" and weather != "cold" and weather != "rainy":
            print("❗ Sorry, I don't recognize that weather type. Try: hot, cold, or rainy.")
            print(" ")
            time.sleep(0.5)
        else:
            break
    
    while True:
        activity = input("🎮 What activities are you planning? (swimming / hiking / business or done) ").lower()
        print(" ")
        time.sleep(0.5)
        if activity == "swimming":
            if swimming == False:
                activityes.append(activity.capitalize())
                print("Adding swimming to the list of activity... 🌊")
                print(" ")
                time.sleep(2.5)
                print("Added! ➕")
                print(" ")
                swimming = True
            else:
                print("❗ Swimming in the list!")
                print(" ")
        elif activity == "hiking":
            if hiking == False:
                activityes.append(activity.capitalize())
                print("Adding hiking to the list of activity... ⛺")
                print(" ")
                time.sleep(2.5)
                print("Added! ➕")
                print(" ")
                hiking = True
            else:
                print("❗ Hiking in the list!")
                print(" ")
        elif activity == "business":
            if business == False:
                activityes.append(activity.capitalize())
                print("Adding business to the list of activity... 💰")
                print(" ")
                time.sleep(2.5)
                print("Added! ➕")
                print(" ")
                business = True
            else:
                print("❗ Business in the list!")
                print(" ")
        elif activity == "done":
            if activityes != []:
                print("👌 All activity is wrote, okay!")
                print(" ")
                break
            else:
                print("❗ No activity!")
                print(" ")
                sure_no_activity = input("❓ Are you sure about no extra items for activity? (Yes - sure, no - not sure) ").lower()
                print(" ")
                if sure_no_activity == "yes":
                    print("👌 Okay! No activity!")
                    print(" ")
                    activityes.append("No activity")
                    break
                elif sure_no_activity == "no":
                    continue
                else:
                    print("❗ Sorry, I don't recognize that choice, try again!")
                    print(" ")
                    continue
        else:
            print(" ❗Sorry, I don't recognize that activity. Try: swimming, hiking, business, or done.")
            print(" ")
            continue
    
    while True:
        days = input("⏳ How many days will your trip last? ")
        print(" ")
        if days.isdigit():
            if int(days) <= 0:
                print("❗ Please enter a valid number of days!")
                print(" ")
                continue
            if int(days) > 0:
                break
        else:
            print("❗ Please enter a valid number of days!")
            print(" ")
            continue
    
    return activityes, weather, int(days)

def packing_list(weather, days, activityes, package_for_trip):
    b_it = package_for_trip[0]
    w_it = package_for_trip[1]
    a_it = package_for_trip[2]
    s_a_u = package_for_trip[3]

    b_it = ["Toothpaste and toothbrush", "Phone charger", "Passport / ID", "Wallet", "Medications (if needed)"]

    if weather == "hot":
        w_it = ["Sunglasses", "Sunscreen", "Shorts", "Light T-shirts", "Sandals", "Hat"]
    elif weather == "rainy":
        w_it = ["Umbrella", "Raincoat", "Waterproof shoes", "Plastic bag for wet clothes"]
    elif weather == "cold":
        w_it = ["Warm jacket", "Winter hat", "Gloves", "Thermal underwear", "Warm socks", "Scarf"]

    if "Hiking" in activityes:
        a_it.append(["Hiking boots", "Backpack", "Water bottle", "First aid kit"])
    if "Swimming" in activityes:
        a_it.append(["Swimsuit", "Beach towel", "Flip-flops", "Waterproof phone case"])
    if "Business" in activityes:
        a_it.append(["Formal suit", "Laptop", "Charger", "Notebook and pen"])
    if "No activity" in activityes:
        a_it.append("No need extra items for this category!")
    
    s_a_u = days + 1

    print("🧳 Generating your packing list...")
    print(" ")
    time.sleep(2.5)
    print("=== Your Packing List ===")
    print(" ")
    time.sleep(0.5)
    iteration = 0
    for it in b_it:
        if iteration == 0:
            print("🏡  Base essentials: ", end = "")
        print(it, end = "; ")
        iteration += 1
        time.sleep(0.5)
    iteration = 0
    print(" ")
    print(" ")
    for it in w_it:
        if iteration == 0:
            print(f"🌦️  Weather items ({weather}): ", end = "")
        print(it, end = "; ")
        iteration += 1
        time.sleep(0.5)
    iteration = 0
    print(" ")
    print(" ")
    for it in a_it:
        if iteration == 0:
            print(f"🎮  Activity items ({activityes}): ", end = "")
        print(it, end = "; ")
        iteration += 1
        time.sleep(0.5)
    iteration = 0
    print(" ")
    print(" ")
    print(f"👕  Clothing (for {days} days): ", end = "")
    time.sleep(0.5)
    print(f"You'll need approximately {s_a_u} pairs of socks and underwear.")
    print(" ")
    if days > 7:
        print(f"⚠️ Your trip is longer than 7 days - you might want to plan for laundry!")
        print(" ")
        print("✅ Your packing list is ready. Have a great trip!")
        print(" ")
    else:
        print("✅ Your packing list is ready. Have a great trip!")
        print(" ")

print("=== ✈️  Smart Packing Assistant ===")
print(" ")
time.sleep(0.5)
print("👋 Welcome! Let's help you pack for your trip.")
print(" ")
time.sleep(0.5)
while True:
    print("❓ Choose what to do:")
    print("1. Create a new packing list 1️⃣")
    print("2. Exit the program 2️⃣")
    print(" ")
    time.sleep(0.5)
    choice = input("🔢 Enter your choice: ")
    print(" ")
    time.sleep(0.5)
    if choice.isalpha():
        print("❗ Choice can't be letter!")
        print(" ")
        time.sleep(0.5)
        continue
    elif choice.isdigit():
        choice = int(choice)
        if choice == 1:
            activityes, weather, days = info_of_trip()
            print(" ")
            time.sleep(0.5)
            packing_list(weather, days, activityes, package_for_trip)
            time.sleep(0.5)
        elif choice == 2:
            print("Thanks for using Smart Packing Assistant! ✨")
            print(" ")
            time.sleep(0.5)
            print("Goodbye and have a safe trip! 👋")
            break
    elif choice.strip() == "":
        print("❗ Choice can't be empty!")
        print(" ")
        time.sleep(0.5)
        continue
    else:
        print("❗ Choice can't be letter!")
        print(" ")
        time.sleep(0.5)
        continue
