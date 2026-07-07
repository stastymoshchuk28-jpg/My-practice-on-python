#Not done!
import time

def analyze_text(text):
    only_up = False
    only_low = False
    upper_letter = False
    lower_letter = False
    number_letter = False
    vowels = 0
    sentences = 0
    len_of_text = len(text)
    for let in text:
        if let.isupper():
            upper_letter = True
        elif let.islower():
            lower_letter = True
        elif let.isdigit():
            number_letter = True
        elif let == "." or let == "!" or let == "?":
            sentences += 1
        
    for let in text:
        if let in "aeiou" or let in "AEIOU":
            vowels += 1
    
    if text.lower() == text:
        only_low = True
    elif text.upper() == text:
        only_up = True
    
    return only_up, only_low, upper_letter, lower_letter, number_letter, vowels, sentences, len_of_text

print("===Text Statistics Analyzer===")
print(" ")
while True:
    print("Choose what to do:")
    print("1. Write new text and analyze it!")
    print("2. Exit the proggram")
    print(" ")
    choose_do = input("Choose number of action: ")
    time.sleep(1)
    if choose_do.isalpha():
        print(" ")
        print("Choose can't be letter! Try again!")
        continue
    elif choose_do.isdigit():
        print(" ")
        choose_do = int(choose_do)
        if choose_do == 1:
            text = input("Okay, firstly write the text: ")
            new_text = text.strip()
            print(" ")
            if new_text[-1 : : ] != "." and new_text[-1 : : ] != "!" and new_text[-1 : : ] != "?":
                new_text = new_text + "."
            time.sleep(1)
            print("🔍 Analizyng your text")
            print(" ")
            up_text, low_text, upper_letter, lower_letter, numbers, vowels, sentences, len_of_text = analyze_text(new_text)
            time.sleep(5)
            print("=== Stats of text: ===")
            print(" ")
            time.sleep(1)
            if up_text:
                print("Your text only in upper case!")
                print(" ")
                time.sleep(1)
            elif low_text:
                print("Your text only in lower case!")
                print(" ")
                time.sleep(1)
            else:
                if lower_letter:
                    print("In your text there are lower case letters!")
                    print(" ")
                    time.sleep(1)
                if upper_letter:
                    print("In your text there are upper case letters!")
                    print(" ")
                    time.sleep(1)

            if numbers:
                print("In text there are numbers!")
                print(" ")
                time.sleep(1)
            
            print(f"In your text there are {vowels} vowels!")
            print(" ")
            time.sleep(1)

            if sentences > 0:
                print(f"In text there {sentences} sentences!")
                print(" ")
                time.sleep(1)
            
            print(f"Your text {len_of_text} len!")
            print(" ")
            print("======")
            time.sleep(1)
            
        elif choose_do == 2:
            print("Thank's for using proggram!")
            print(" ")
            print("Goodbye!")
            break
        else:
            print("Not right number! Try again!")
            print(" ")
            continue
        print(" ")