from time import sleep
#Not done
#v0.1

books = set()
it = 1

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def menu(it):
    while True:
        print("=== 📚 Library Inventory Manager ===")
        oformity1()
        if it == 1:
            print("👋 Welcome! Let's manage your library.")
            oformity1()
        print("Choose what to do:")
        oformity1()
        print("...")
