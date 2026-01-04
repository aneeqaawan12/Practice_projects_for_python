import random

top_range = int(input("Write a number for top range: "))
if top_range <= 0:
    print("Enter a number greater than 0. ")
    quit()

secret_number = random.randint(0, top_range)
guess_count = 0
while True:
    guess_count += 1
    number_guess = input("Enter a number to guess: ")
    if number_guess.isdigit():
        number_guess = int(number_guess)
    else:
        print("Enter a valid number. ")
        continue

    if number_guess == secret_number:
        print("you guess it right;) ")
        break
    elif number_guess < secret_number:
        print("You are below the secret number. ")
    else:
        print("You are above the secret number. ")

print("you guess it in", guess_count, "turns!")