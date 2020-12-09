import random

word_list = ["india", "pakistan", "america"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"
print(display)

lives = 8
game_over = False
while not game_over:
    guess = input("Enter a guess : ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        lives -= 1
    if lives == 0:
            game_over = True
            print("You Lose")
    print(display)

    if "_" not in display:
        game_over = True
        print("Yow Win")