import random

user_scores = 0
computer_scores = 0

inputs = ["rock", "paper", "scissor"]
while True:
    user_input = input("Enter rock/paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in inputs:
        print("Enter rock/paper/scissor only to proceed. ")
        continue

    computer_turns = random.randint(0, 2)
    # 0 for rock, 1 for paper, 2 for scissor
    computer_picks = inputs[computer_turns]
    print("Computer picked", computer_picks + ".")


    if user_input == "rock" and computer_picks == "scissor":
        print("you win!")
        user_scores += 1
    elif user_input == "paper" and computer_picks == "rock":
        print("you win!")
        user_scores += 1
    elif user_input == "scissor" and computer_picks == "paper":
        print("you win!")
        user_scores += 1

    else:
        print("Computer wins! ")
        computer_scores += 1

print("You won", user_scores, "times. ")
print("computer won", computer_scores, "times")
print("Happy playing. Goodbye! ")

