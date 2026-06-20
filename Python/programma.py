print("=== Secret Message Encoder ===")
while True:
    print("User, choose action please:")
    print("1 - Encrypt message")
    print("2 - Decrypt message")
    print("3 - Exit")
    choosing_action = int(input("Enter action number: "))
    print("==============================")
    if choosing_action == 1:
        encrypted_message = ""
        message = input("Enter your message: ")
        shift = int(input("Enter shift (1-25): "))
        order_letter = 0
        new_letter = ""
        for let in message:    
            if (ord(let) >= 65 and ord(let) <= 90) or (ord(let) >= 97 and ord(let) <= 122):
                order_letter = ord(let) + shift
                new_letter = chr(order_letter)
                encrypted_message = encrypted_message + new_letter
                order_letter = 0
                new_letter = ""
            else:
                encrypted_message = encrypted_message + let
        print(f"Encrypted: {encrypted_message}")
        print("==============================")
    elif choosing_action == 2:
        message = input("Enter your message: ")
        shift = int(input("Enter shift (1-25): "))
        decrypted_message = ""
        order_letter = 0
        new_letter = ""
        for let in message:
            if (ord(let) >= 65 and ord(let) <= 90) or (ord(let) >= 97 and ord(let) <= 122):
                order_letter = ord(let) - shift
                new_letter = chr(order_letter)
                decrypted_message = decrypted_message + new_letter
                order_letter = 0
                new_letter = ""
            else:
                decrypted_message = decrypted_message + let
        print(f"Decrypted: {decrypted_message}")
        print("==============================")
    elif choosing_action == 3:
        print("Thanks for using proggram!")
        break
    else:
        print("Action number is not right")
        print("Please, try again!")
        print("==============================")
        continue