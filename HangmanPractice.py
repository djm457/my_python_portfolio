#!/usr/bin/env python3

#game introduction
print("-"*60)
print(' Welcome to he hangman game. I am using this to improve my Python capabilities.\n', \
      'The code as the foundation for this script may be found at: \n https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman/ \n',
      'I will also be uploading this script to learn Git. I make no claim that this is code I developed.')
print("-"*60)



def game_engine():
    #game settings
    secret_word = "secret"
    guesses = []
    solution_display = []
    game_rounds = 7

    #game mechanics 
    while game_rounds > 0:
        failed = 0
        guess = input("Guess a character: ")
        if guess in secret_word:
            print('correct guess\n')
            solution_display.append(guess)
            
            for char in secret_word:
                if char in solution_display:
                    print(char)
                else:
                    print('-')
                    failed += 1
                   
        else:
            game_rounds -= 1
            failed = 1
            guesses.append(guess)
            print("\n{} was incorrect. Try again. \n".format(guess))
            print("ALL LETTERS GUESSED: {} \nCORRECT GUESSES: {} \nREMAINING TURNS: {} \n".format(guesses, solution_display, game_rounds))

        if failed == 0:
            print("You won!")
            break
            
    if game_rounds == 0:
        print("You Loser!")
        play_again()
      

def play_again():
    answer = input("Would you like to play again? Entter 'y' for yes or press any other key to exit: ")
    if answer.lower() == 'y':
        return True
       



#Welcome the user
user_name = input("Enter your name: ")
print("\n")
print("Welcome to the game {}.\n".format(user_name))

game_engine()
        


   

            
        
  



        
    
