#!/usr/bin/env python3


import re
    
def game_settings_input(prompt, type_=None, max_=None, secret_word=None):
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
        if max_ is not None and ui < 1:
            print("Input must be greater than or equal to 1.")
        elif secret_word is not None and ui.isdigit():
            print("Input must be a string.")
        elif secret_word is not None and bool(re.findall("\W", ui)) == True:
            print("Input must not contain special characters.")
        else:
            return ui
                
    
number_of_turns = game_settings_input("Enter number of turns: ", int, 4)
the_secret_word = game_settings_input("Enter the secret word: ", str.lower, secret_word = "test")


          
    
    
#validation references
#https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response



