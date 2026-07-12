from time import sleep

riddles = ["I have keys but no locks. I have space but no room. You can enter, but you can't go outside. What am I?", "The more you take, the more you leave behind. What am I?", "What has hands but cannot clap?", "What gets wetter the more it dries?", "I am not alive, but I can grow. I don't have lungs, but I need air. What am I?", "What can travel around the world while staying in one corner?", "What has a neck but no head?", "What comes once in a minute, twice in a moment, but never in a thousand years?"]
riddle_number = 1
total_number_of_riddle = 8
points = 0

def riddle(riddle, riddles, riddle_num, total_number_of_riddle, points):
    print(f"🧩 Riddle: {riddle}")
    print(" ")
    def create_answer(riddles, riddle):
        if riddles[0] == riddle:
            answer = "keyboard"
        elif riddles[1] == riddle:
            answer = "footsteps"
        elif riddles[2] == riddle:
            answer = "clock"
        elif riddles[3] == riddle:
            answer = "towel"
        elif riddles[4] == riddle:
            answer = "fire"
        elif riddles[5] == riddle:
            answer = "stamp"
        elif riddles[6] == riddle:
            answer = "bottle"
        elif riddles[7] == riddle:
            answer = "m"
        return answer
    def create_hint(riddles, riddle):
        ...
    hint = create_hint(riddles, riddle)
    correct_answer = create_answer(riddles, riddle)
    attemtps = 3

    print(f"🔢 Riddle {riddle_num} of {total_number_of_riddle}:")
    while True:
        user_answer = input("⌨️ Type your answer, or type 'hint' for a clue, or 'skip' to move on: ").strip()
        print(" ") 
        if user_answer.lower() == correct_answer:
            print("🎉 Correct! Well done!")
            riddle_num += 1
            points += 10
            return riddle_num, points
        elif user_answer.lower() != correct_answer:
            print("❌ Not quite, try again!")
            attemtps -= 1
            continue
        elif user_answer.lower() == "hint":
            print("💡 Here's a hint for you: ")

print("=== 🧩 Riddle Master ===")
print(" ")
sleep(0.5)
print("👋 Welcome! Test your brain with some classic riddles.")
print(" ")
sleep(0.5)

while True:
    print("❓ Choose what to do:")
    print("1️⃣  1. Start the game")
    print("2️⃣  2. Exit")
    print(" ")
    sleep(0.5)
    choice = input("⌨️ Enter your choice: ")
    print(" ")
    sleep(0.5)
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            for rid in riddles:
                riddle_number, points = riddle(rid, riddles, riddle_number, total_number_of_riddle, points)