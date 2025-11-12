import random

number = random.randint (1, 100)
guess = input ("guess number\n>")
while guess == number:
    guess = input ("guess number\n>")
    guess = int(guess)
    if guess < number:
        print ("you are to low")
    elif guess > number:
        print("you are to high")
    elif guess == number:
        print ("good job")

