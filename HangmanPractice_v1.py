#!/usr/bin/env python3


import re
    
def game_settings_input(prompt, type_=None, max_=None, secret_word=None):
    '''Sets the game settings: # of turns for player and the secret word the player will guess.'''
    if max_ is not None and max_ < 1:
        raise ValueError("max_ must be greater than 0.")
    while True:
        ui = input(prompt)
        if type_ is not None:
            try:
                ui = type_(ui)
            except ValueError:
                print("Input type must be {}.".format(type_.__name__))
                continue
        #validate digit entered for turns is 1 or greater
        if max_ is not None and ui < 1:
            print("Input must be greater than or equal to 1.")
        #validate secret word is not a digit
        elif secret_word is not None and ui.isdigit():
            print("Input must be a string.")
        #validate secret word is not a special character
        elif secret_word is not None and bool(re.findall("\W", ui)) == True:
            print("Input must not contain special characters.")
        else:
            return ui
                
#calls the function passing the parameters for each game setting.    
number_of_turns = game_settings_input("Enter number of turns: ", int, 4)
the_secret_word = game_settings_input("Enter the secret word: ", str.lower, secret_word = "test")
        
    
#validation references
#https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
def confirm_game_settings(prompt, type_=None, confirmation=None):
    '''Confirm the game settings are accurate. If not, then re-enter the game settings'''
    while True:
        con = input(prompt)
        if type_ is not None:
            try:
                con = type_(con)
            except ValueError:
                print("Input type must be {}.".format(type_.__name__))
                continue
        #validate that a single character is entered into the prompt
        if confirmation is not None and len(con) != 1:
            print("Input must be either Y or N.")
        #validate only Y or N is entered into the prompt
        elif confirmation is not None and bool(re.findall("n|y", con)) == False:
            print("Input must be either Y or N.")
        #validate no special characters are entered into the prompt
        elif confirmation is not None and bool(re.findall("\W", con)) == True:
            ("Input must be either Y or N.")
        #reset the settings if N is entered into the prompt
        elif con.lower() == "n":
            print("\nSettings Reset\n")
            number_of_turns = game_settings_input("Enter number of turns: ", int, 4)
            the_secret_word = game_settings_input("Enter the secret word: ", str.lower, secret_word = "test")
        else:
            break

                    
settings_confirmation = confirm_game_settings("Are the settings correct? Y/N: ", str.lower, confirmation = "n")










