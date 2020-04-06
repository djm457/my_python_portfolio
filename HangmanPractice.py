#!/usr/bin/env python3

print("-"*60)
print(' Welcome to he hangman game. I am using this to improve my Python capabilities.\n', \
      'The code as the foundation for this script may be found at: \n https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman/ \n',
      'I will also be uploading this script to learn Git. I make no claim that this is code I developed.')
print("-"*60)

#Welcome user
user_name = input("Enter your name: ")
print("Welcome {} to the game.".format(user_name))


#Game attributes
secret_word = "secret"
guesses = []
solution_display = []
game_rounds = 7



#Game engine
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
        guesses.append(guess)
        print("ALL LETTERS GUESSED: {} \nCORRECT GUESSES: {} \nREMAINING TURNS: {}".format(guesses, solution_display, game_rounds))

    if failed == 0:
        print("You won!")
        break   
    if game_rounds == 0:
        print("You Loser!")


   

            
        
  



        
    
