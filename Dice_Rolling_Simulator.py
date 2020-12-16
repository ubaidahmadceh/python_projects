from random import randint
while True:
    user_input = int(input("Enter '1' to roll a dice\nOR '2' to quit : \n"))
    rolled_dice_number = randint(1,6)
    if user_input == 1:
        print("Rolled Dice Number is :", rolled_dice_number)
    elif user_input == 2:
        break
    else:
        print("Please Enter '1' OR '2'")
print("Thankyou for playing")