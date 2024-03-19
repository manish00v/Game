# Copyright 2023 Bruno Zhong
import math
import random
import time

wins = 0
ties = 0
defeats = 0
turns = 0
possible = ["Rock", "Paper", "Scissors"]
ans = ""
botAns = ""

startTime = time.monotonic()
for i in range(10):
    ans = input("Rock, paper, or scissors?")
    randInt = math.floor(random.random() * 3)
    botAns = possible[randInt]
    time.sleep(1)
    print(f"The bot chose {botAns.lower()}.")
    turns += 1
    time.sleep(1)
    if ans.lower() == botAns.lower():
        print("It was a tie!")
        ties += 1
    elif ans.lower() == "paper" and botAns.lower() == "rock":
        print("You won!")
        wins += 1
    elif ans.lower() == "rock" and botAns.lower() == "scissors":
        print("You won!")
        wins += 1
    elif ans.lower() == "scissors" and botAns.lower() == "paper":
        print("You won!")
        wins += 1
    else:
        print("You lost!")
        defeats += 1
    time.sleep(1)

endTime = time.monotonic()

print(f"You played for {endTime - startTime} seconds!")
print(f"You won {wins} out of {turns} games!")
time.sleep(1)
print(f"You tied {ties} out of {turns} games!")
time.sleep(1)
print(f"You lost {defeats} out of {turns} games!")

time.sleep(1)

if (wins / turns) > 0.8:
    print("Great job!")
elif (wins / turns) > 0.6:
    print("Good job!")
elif ((wins + ties) / turns) > 0.4:
    print("Can you do better?")
else:
    print("Practice makes perfect!")
