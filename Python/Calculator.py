#Done
#v1.0

from time import sleep

operator_list = ["+", "-", "*", "/", "%", "**"]

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)
    
def find_first_number():
    try:
        first_number = float(input("⌨️  Enter first number: "))
        pause_long()
        return False, first_number
    except ValueError:
        pause_long()
        print("❗ You need to enter number. Like 12 or 15.9!")
        pause_long()
        return True, 0
    
def operator():
    def check_operator(operator):
        if operator == "+":
            return "add"
        elif operator == "-":
            return "sub"
        elif operator == "*":
            return "mul"
        elif operator == "/":
            return "div"
        elif operator == "%":
            return "mod"
        elif operator == "**":
            return "exp"
        else:
            return "Nil"
    operator = input("⌨️  Enter operator: ").strip()
    pause_long()
    if operator in operator_list:
        action = check_operator(operator)
        if action == "Nil":
            print("❗ Not right operator!")
            return True, action
        else:
            return False, action
    else:
        return True, "Nil"

def find_second_number():
    try:
        second_number = float(input("⌨️  Enter second number: "))
        pause_long()
        return False, second_number
    except ValueError:
        pause_long()
        print("❗ You need to enter number. Like 12 or 15.9!")
        pause_long()
        return True, 0

def action(a, f, s):
    def add(f, s):
        result = f + s
        print(f"✅ Result: {result}")
        pause_long()

    def sub(f, s):
        result = f - s
        print(f"✅ Result: {result}")
        pause_long()

    def mul(f, s):
        result = f * s
        print(f"✅ Result: {result}")
        pause_long()

    def div(f, s):
        try:
            result = f / s
            print(f"✅ Result: {result}")
            pause_long()
        except ZeroDivisionError:
            print("❗ Can't do division by zero!")
            pause_long()

    def exp(f, s):
        try:
            result = f ** s
            print(f"✅ Result: {result}")
            pause_long()
        except OverflowError:
            print("❗ Can't do this calculation! It's too big! More than infinity!")
            pause_long()

    def mod(f, s):
        try:
            result = f % s
            print(f"✅ Result: {result}")
            pause_long()
        except ZeroDivisionError:
            print("❗ Can't do division by zero!")
            pause_long()            

    if a == "add":
        add(f, s)
    elif a == "sub":
        sub(f, s)
    elif a == "mul":
        mul(f, s)
    elif a == "div":
        div(f, s)
    elif a == "mod":
        mod(f, s)
    elif a == "exp":
        exp(f, s)
    else:
        print("❗ Error!")
        pause_long()

while True:
    print("=== Calculator ===")
    pause_long()
    to_continue, first_number = find_first_number()
    if to_continue:
        continue
    to_continue, found_action = operator()
    if to_continue:
        continue
    to_continue, second_number = find_second_number()
    if to_continue:
        continue
    action(found_action, first_number, second_number)
    want_to_continue = input("⌨️  Enter do you want to continue calculations? (yes/no) ").strip()
    pause_long()
    if want_to_continue == "yes":
        print("✨ Continue calculator!")
        pause_long()
        continue
    elif want_to_continue == "no":
        print("👋 Goodbye!")
        pause_long()
        break
    else:
        print("❗ You need to enter yes or no!")
        pause_long()
        print("❗ Continue calculator!")
        pause_long()
        continue
