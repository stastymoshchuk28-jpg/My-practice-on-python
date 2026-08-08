from time import sleep

operator_list = ["+", "-", "*", "/", "%", "**"]

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)
    
def find_first_number():
    try:
        first_number = float(input("⌨️  Enter first number: "))
        oformity1()
        return False, first_number
    except ValueError:
        oformity1()
        print("❗ You need to enter number. Like 12 or 15.9!")
        oformity1()
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
    oformity1()
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
        oformity1()
        return False, second_number
    except ValueError:
        oformity1()
        print("❗ You need to enter number. Like 12 or 15.9!")
        oformity1()
        return True, 0

def action(a, f, s):
    def add(f, s):
        result = f + s
        print(f"✅ Result: {result}")
        oformity1()

    def sub(f, s):
        result = f - s
        print(f"✅ Result: {result}")
        oformity1()

    def mul(f, s):
        result = f * s
        print(f"✅ Result: {result}")
        oformity1()

    def div(f, s):
        try:
            result = f / s
            print(f"✅ Result: {result}")
            oformity1()
        except ZeroDivisionError:
            print("❗ Can't do division by zero!")
            oformity1()

    def exp(f, s):
        try:
            result = f ** s
            print(f"✅ Result: {result}")
            oformity1()
        except OverflowError:
            print("❗ Can't do this calculation! It's too big! More than infinity!")
            oformity1()

    def mod(f, s):
        try:
            result = f % s
            print(f"✅ Result: {result}")
            oformity1()
        except ZeroDivisionError:
            print("❗ Can't do division by zero!")
            oformity1()            

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
        oformity1()

while True:
    print("=== Calculator ===")
    oformity1()
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
    oformity1()
    if want_to_continue == "yes":
        print("✨ Continue calculator!")
        oformity1()
        continue
    elif want_to_continue == "no":
        print("👋 Goodbye!")
        oformity1()
        break
    else:
        print("❗ You need to enter yes or no!")
        oformity1()
        print("❗ Continue calculator!")
        oformity1()
        continue
