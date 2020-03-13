from random import randint

secret_number = randint(1,10)
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False

while guess != secret_number and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter a number: ")
        guess_count += 1
        if int(guess) > int(secret_number):
            print("Lower")
        elif int(guess) == int(secret_number):
            print("You win!")
        else:
            print("Higher")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")



