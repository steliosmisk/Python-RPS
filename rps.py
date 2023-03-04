import os
import random

print("--WELCOME TO RPS GAME--")
print("[1] Start The Game")
print("[2] Exit")

# AI Action
ai_action = random.choice(["rock", "paper", "scissors"])

user_choice = input("Enter (1/2): ")

while user_choice == "1" and user_choice != "2":
    user_action = input("(R)ock, (P)aper or (S)cissors?: \n").lower()

    if user_action == ai_action:
        print(f"YOU: {user_action} | AI: {ai_action}, TIE!")
    elif user_action in ["r", "rock"]:
        if ai_action == "scissors":
            print(f"YOU: {user_action} | AI: {ai_action}, You Win!")
        else:
            print(f"YOU: {user_action} | AI: {ai_action}, You Lost!")
    elif user_action in ["p", "paper"]:
        if ai_action == "rock":
            print(f"YOU: {user_action} | AI: {ai_action}, You Win!")
        else:
            print(f"YOU: {user_action} | AI: {ai_action}, You Lost!")
    elif user_action in ["s", "scissors"]:
        if ai_action == "paper":
            print(f"YOU: {user_action} | AI: {ai_action}, You Win!")
        else:
            print(f"YOU: {user_action} | AI: {ai_action}, You Lost!")
    else:
        os.system("cls")
        print("Enter a valid action!")
