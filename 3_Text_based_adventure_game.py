print("Welcome to tresure Island")
print("Your mission is to Find the Treasure")
Choice_1 = input("You are at a crossroad, where do you want to go? Type 'left' or 'right'.\n").lower()

if Choice_1 == "left":
    Choice_2 = input("you have come to a lake, There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n").lower()
    if Choice_2 == "wait":
        choice_3 = input("You arrive at the island unharmed. There is a house With 3 doors. One red, one yellow and one blue.\n Which color do you choose?\n").lower()
        if choice_3 == "red":
            print("It is a room full of fire. Game Over.")
        elif choice_3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice_3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by angry lion. Game Over.")
else:
    print("You fell into a hole. Game Over.")