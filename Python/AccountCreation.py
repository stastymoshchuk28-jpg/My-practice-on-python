game = "Magic world of Python"

print(f"Welcome to the {game}!")
print(" ")
print("Welcome to the account creation process!")
print(" ")
print("Please follow the instructions to create your account.")
print(" ")
name = input("Create your unusual username for account: ").capitalize()
print(" ")
password = input("Create your password for account: ")
print(" ")
if len(password) < 8:
    print(f"The {password} must be at least 8 characters long. Please try again.")
    password = input("Create your password for account: ")
else:
    print(f"{name}, your account has been created successfully!")
print(" ")
print(f"So now {name} have an account, you need to create your character to play the game.")
print(" ")
print("Please follow the instructions to create your character.")
print(" ")
name_character = input("Create your character name: ").capitalize()
print(" ")
print(f"{name_character} is a great name for your character!")
print(" ")
print("Now you need to choose your character class.")
print(" ")
print("1. Warrior")
print("2. Mage")
print("3. Archer")
print(" ")
class_choice = int(input("Please enter the number corresponding to your character class: "))
print(" ")
if class_choice == 1:
    character_class = "Warrior"
elif class_choice == 2:
    character_class = "Mage"
elif class_choice == 3:    
    character_class = "Archer"
else:
    print("Invalid choice. Please try creating your character again.")
print(f"You have chosen the {character_class} class for your character.")
print(" ")
print(f"Congratulations {name_character}, you have successfully created your character as a {character_class}!")
print(" ")
print("Now {name} are ready to start your adventure in the Magic world of Python!")