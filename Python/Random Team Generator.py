import time
import random

names = []
peoples = 0

team1 = []
team2 = []
team3 = []

teams = [team1, team2, team3]

def namess(names, peoples):
    while True:
        name = input("Write name for teams (or Done for finish): ").capitalize()
        print(" ")
        time.sleep(0.5)
        if name == "Done":
            return names, peoples
        if name == " " or name == "":
            continue
        if not name.isdigit():
            letters = 0
            for let in name:
                if let == " " or let.isalpha():
                    letters += 1
            if letters == len(name):
                if name.strip() != "":
                    print("Name added to list!")
                    print(" ")
                    names.append(name)
                    peoples += 1
                    time.sleep(0.5)
                    continue
                else:
                    print("Sorry, i can't add this name to list!")
                    print(" ")
                    time.sleep(0.5)
                    continue
            else:
                print("Sorry, i can't add this name to list!")
                print(" ")
                time.sleep(0.5)
                continue
        else:
            print("Sorry, i can't add this name to list!")
            print(" ")
            time.sleep(0.5)
            continue

def names_in_teams(names, teams):
    for name in names:
        random_team = random.choice(teams)
        random_team.append(name)
        print(f"{name} added to team.")
        print(" ")
        time.sleep(0.5)
    return teams
print("=== Random Team Generator === ")
print(" ")
time.sleep(0.5)
print("Here only 3 teams. Write names and they will split into teams")
print(" ")
time.sleep(0.5)
names, peoples = namess(names, peoples)
time.sleep(0.5)
team1, team2, team3 = names_in_teams(names, teams)
print(f"Peoples: {peoples}")
time.sleep(0.5)
print(f"Names: {names}")
print(" ")
time.sleep(0.5)
print("Teams:")
print(f"Team 1: {team1}")
time.sleep(0.5)
print(f"Team 2: {team2}")
time.sleep(0.5)
print(f"Team 3: {team3}")