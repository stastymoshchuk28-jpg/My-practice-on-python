#Done
#v1.0
import time

count_calculations = 0

print("=== Smart Calculator Bot ===")
print(" ")
print("👋 Hello!")
print(" ")
print("✨ I can: +, -, *, /, ** (power)")
print(" ")
time.sleep(0.5)
print("⚡ Let's start our calculations!")
print(" ")

def add(a, b):
     result = a + b
     return result

def substract(a, b):
     result = a - b
     return result

def multiply(a, b):
     result = a * b
     return result

def divide(a, b):
     result = a / b
     return result

def power(a, b):
     result = a ** b
     return result

while True:

    first_number = float(input("1️⃣  Enter first number: "))
    print(" ") 
    operator = input("➕ ➖ ✖️  ➗  Enter operator (+ or other in list): ")
    print(" ")
    time.sleep(0.5)
    second_number = float(input("2️⃣  Enter second number: "))

    if operator == "+":
        result = add(first_number, second_number)
        print(" ")
        time.sleep(0.5)
        print(f"🌟 Result of calculation - {result}")
        count_calculations += 1
    elif operator == "-":
        result = substract(first_number, second_number)
        print(" ")
        time.sleep(0.5)
        print(f"🌟 Result of calculation - {result}")
        count_calculations += 1
    elif operator == "*":
        result = multiply(first_number, second_number)
        print(" ")
        time.sleep(0.5)
        print(f"🌟 Result of calculation - {result}")
        count_calculations += 1
    elif operator == "/":
        if second_number == 0:
            print("🤖 Division by zero detected! Even I can't break math like that 😅")
            print(" ")
            time.sleep(0.5)
            continue
        else:
            result = divide(first_number, second_number)
            print(" ")
            time.sleep(0.5)
            print(f"🌟 Result of calculation - {result}")
            count_calculations += 1
    elif operator == "**":
        result = power(first_number, second_number)
        print(" ")
        time.sleep(0.5)
        print(f"🌟 Result of calculation - {result}")
        count_calculations += 1
    else:
        print(" ")
        print("❗ Sorry, i can't do that calculation!")
        print(" ")
        time.sleep(0.5)
        continue
    
    print(" ")
    want_continue = input("❓ Continue? (yes/no): ").lower()
    time.sleep(0.5)
    if want_continue == "yes":
        print(" ")
        print("✅ Continue calculations!")
        print(" ")
        time.sleep(0.5)
        continue
    elif want_continue == "no":
        print(" ")
        print("❗ Okay, stoping calculations!")
        time.sleep(0.5)
        print(" ")
        print("=== Session Summary ===")
        time.sleep(0.5)
        print(" ")
        print(f"✨ Total operations: {count_calculations}!")
        time.sleep(0.5)
        print(" ")
        print("👋 Goodbye!")
        break
    else:
        print(" ")
        print("❗ Not right choose, continue calculations!")
        time.sleep(0.5)
        continue