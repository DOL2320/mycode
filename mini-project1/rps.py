#!/usr/bin/python3
"""Rock, paper, scissors | Author: Dorian Majano"""
import random # import modules

def main():
    cpu_picks = ['rock', 'paper', 'scissors'] # create a list to store cpu picks

    # keep score
    user_score = 0
    cpu_score = 0

    print("Welcome to Rock, Paper, Scissors. First player to 5 wins!")

    # break the loop if either player scores five
    while user_score < 5 and cpu_score < 5:
        # Collect user input
        user_input = input("Make a selection (Rock, Paper, Scissors): ").capitalize()

        # Validate user input. Should be non-empty and either Rock, Paper, or Scissors
        if not user_input or user_input != 'Rock' and user_input != 'Paper' and user_input != 'Scissors':
            continue

        cpu_pick = cpu_picks[random.randrange(cpu_picks.__len__())].capitalize()

        print(f"You selected {user_input}, the CPU selected {cpu_pick}")
   
        # strip the first letter of each because that's all we need for our comparisons
        user_input = user_input[0].lower()
        cpu_pick = cpu_pick[0].lower()

        # in case each player picks the same, it's a draw, go again
        if user_input == cpu_pick:
            continue
        elif user_input == 'r' and cpu_pick == 's' or user_input == 'p' and cpu_pick == 'r' or user_input == 's' and cpu_pick == 'p':
            user_score += 1
            print(f"Your score: {user_score}\nCPU score: {cpu_score}")
        else:
            cpu_score += 1
            print(f"Your score: {user_score}\nCPU score: {cpu_score}")

    if cpu_score < user_score:
        print("You win!")

    else:
        print("You lose :(")

main()
