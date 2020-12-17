from random import randint
number = randint(1,11)
no_of_guess = 1
while True:
    guess = int(input("Guess a number between 1 - 10 : "))
    if guess == number:
        print(f"you win this game in {no_of_guess} guess")
        break
    elif guess > number:
        print("Too large guess")
    elif guess < number:
        print("Too small guess")
    else:
        print("Please guess between 0 to 10")
        
    no_of_guess = no_of_guess + 1
    