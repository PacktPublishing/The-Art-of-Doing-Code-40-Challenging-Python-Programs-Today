#While Loops Challenge 29: Guess the Word App
import random

print("Welcome to the Guess My Word App")

#Create the dict to hold our words
game_dict = {
    "sports":['basketball', 'baseball', 'soccer', 'football', 'tennis', 'curling'],
    "colors":['orange', 'yellow', 'purple', 'aquamarine', 'violet', 'gold'],
    "fruits":['apple', 'banana', 'watermelon', 'peach', 'mango', 'strawberry'],
    "classes":['english', 'history', 'science', 'mathematics', 'art', 'health'],
    }

#Create a list of keys
game_keys = []
for key in game_dict.keys():
    game_keys.append(key)

#The main game loop
playing = True
while playing:
    #Randomly pick the game category and the game word from the game dictionary
    game_category = game_keys[random.randint(0,len(game_keys)-1)]
    game_word = game_dict[game_category][random.randint(0, len(game_dict[game_category])-1)]

    #Build a dashed "-" word to represent the game word
    blank_word = []
    for letter in game_word:
        blank_word.append("-")

    print("Guess a " + str(len(game_word)) + " letter word from the following category: " + game_category.title())

    guess = ""
    guess_count = 0

    #A single round loop
    while guess != game_word:
        #Get a single guess from the user
        print("".join(blank_word))
        guess = input("\nEnter your guess: ").lower()
        guess_count += 1

        #Guess is correct, user won the game
        if guess == game_word:
            print("\nCorrect!  You guessed the word in " + str(guess_count) + " guesses.")
            break

        #Guess is incorrect, user must keep guessing
        else:
            print("That is not correct. let us reveal a letter to help you!")
            #Loop to replace "-" in blank_word to reveal a letter to help user
            swapping = True
            while swapping:
                letter_index = random.randint(0, len(game_word)-1)
                if blank_word[letter_index] == "-":
                    blank_word[letter_index] = game_word[letter_index]
                    swapping = False

    #Ask the user to play again
    choice = input("\nWould you like to play again (y/n): ").lower()
    if choice != 'y':
        playing = False
        print("Thank you for playing the game.")
