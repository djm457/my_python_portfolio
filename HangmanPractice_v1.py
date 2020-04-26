#!/usr/bin/env python3

def game_set_up():
    print("Welcome to the game. In this section the 'host' player will need to \n",
          "enter the game setts e.g. # of turns and the secret word.")

    while True:
        try:
            secret_word = str(input("Enter the secret word: "))
        except ValueError:
            print("That is an invalid entry. Try again.")
            continue
        else:
            break
    while True:
        try:
            number_of_turns = int(input("Enter the number of turns for the game: "))
        except ValueError:
            print("That is an invalid entry. Try again.")
            continue
        else:
            break
        
    
    print("GAME SETTINGS:\nSecret Word: {}\nNumber of Turns: {}".format(secret_word,number_of_turns))

game_set_up()
          
    
    
#validation references
#https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
