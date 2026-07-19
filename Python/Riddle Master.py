from time import sleep

riddles = ["I have keys but no locks. I have space but no room. You can enter, but you can't go outside. What am I?", "The more you take, the more you leave behind. What am I?", "What has hands but cannot clap?", "What gets wetter the more it dries?", "I am not alive, but I can grow. I don't have lungs, but I need air. What am I?", "What can travel around the world while staying in one corner?", "What has a neck but no head?", "What comes once in a minute, twice in a moment, but never in a thousand years?"]
riddle_number = 1
total_number_of_riddle = 8
points = 0
max_points = 80

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
        if riddles[0] == riddle:
            hint = "You're probably touching one right now to type your answer."
        elif riddles[1] == riddle:
            hint = "Think about walking in the sand or snow."
        elif riddles[2] == riddle:
            hint = "It tells you something important every second."
        elif riddles[3] == riddle:
            hint = "You use it right after a shower."
        elif riddles[4] == riddle:
            hint = "It's hot, bright, and dangerous if not controlled."
        elif riddles[5] == riddle:
            hint = "You stick it on an envelope before mailing a letter."
        elif riddles[6] == riddle:
            hint = "You often see this in the kitchen or fridge, holding a drink."
        elif riddles[7] == riddle:
            hint = "It's not a whole word - just a single letter."
        return hint
    hint = create_hint(riddles, riddle)
    correct_answer = create_answer(riddles, riddle)
    attemtps = 3
    claiming_points = 0
    hint_used = False
    print(f"🔢 Riddle {riddle_num} of {total_number_of_riddle}:")
    print(" ")
    sleep(0.5)
    while True:
        if attemtps > 0:
            user_answer = input("⌨️  Type your answer, or type 'hint' for a clue, or 'skip' to move on: ").strip()
            print(" ") 
            sleep(0.5)
            if attemtps > 0:
                if user_answer.lower() == correct_answer:
                    print("🎉 Correct! Well done!")
                    print(" ")
                    sleep(0.5)
                    riddle_num += 1
                    if hint_used == True:
                        print("✅ Correct with a hint! +5 points!")
                        print(" ")
                        sleep(0.5)
                        claiming_points = 5
                        points += claiming_points
                        return riddle_num, points
                    elif hint_used == False:
                        if attemtps < 3 and attemtps > 1:
                            print("✅ Correct on second try! +5 points!")
                            print(" ")
                            sleep(0.5)
                            claiming_points = 5
                            points += claiming_points
                        elif attemtps == 3:
                            print("✅ Correct on first try! +10 points!")
                            print(" ")
                            sleep(0.5)
                            claiming_points = 10
                            points += claiming_points
                        else:
                            print("✅ Correct on last attempt! +2 points!")
                            print(" ")
                            sleep(0.5)
                            claiming_points = 2
                            points += claiming_points
                        return riddle_num, points
                elif user_answer.lower() == "hint":
                    print(f"💡 Here's a hint for you: '{hint}'")
                    hint_used = True
                    print(" ")
                    sleep(0.5)
                    continue
                elif user_answer.lower() == "skip":
                    print(f"⏭️  Skipped! The correct answer was: '{correct_answer}'!")
                    print(" ")
                    sleep(0.5)
                    riddle_num += 1
                    return riddle_num, points
                else:
                    print("❌ Not quite, try again!")
                    print(" ")
                    sleep(0.5)
                    attemtps -= 1
            elif attemtps <= 0:
                print(f"😅 No more attempts left! The correct answer was: '{correct_answer}'!")
                print(" ")
                sleep(0.5)
                points += claiming_points
                return riddle_num, points
        elif attemtps <= 0:
            print(f"😅 No more attempts left! The correct answer was: '{correct_answer}'!")
            print(" ")
            sleep(0.5)
            points += claiming_points
            return riddle_num, points

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
    choice = input("⌨️  Enter your choice: ")
    print(" ")
    sleep(0.5)
    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            for rid in riddles:
                riddle_number, points = riddle(rid, riddles, riddle_number, total_number_of_riddle, points)
            print(f"✨ Your final points: {points} out of {max_points}!")
            print(" ")
            sleep(0.5)
            if points < 40:
                print("Rank: Riddle Novice 🐣 (less than half correct)")
                print(" ")
                sleep(0.5)
            elif points < 80:
                print("Rank: Riddle Solver 🧠 (more than half correct)")
                print(" ")
                sleep(0.5)
            else:
                print("Rank: Riddle Master 👑 (almost all correct)")
                print(" ")
                sleep(0.5)
        elif choice == 2:
            print("👍 Thanks for playing Riddle Master!")
            print(" ")
            sleep(0.5)
            print("👋 Goodbye, keep your brain sharp! 🧩")
            break
        else:
            print("❗ Please enter a valid choice!")
    else:
        print("❗ Please enter a valid choice!")