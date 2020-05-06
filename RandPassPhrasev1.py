#!/usr/bin/python3

import random, string


def RandPassPhrase(length=4):
    '''create a passphrase using a random selection of words from english dictionary, digits, and punctuation'''
    #input each word for the english dictionary stored in a text file on the local hosts file system. 
    with open('C:/Python38/word_lists/english_words_dict/english_words.txt', 'r') as f:
        #reads each word of the english dictionary into a list and capitalizes the first letter of each word.
        english_words = [line.strip().title() for line in f]
    f.close()
    #set the additional characters to be added to the phrase
    options = string.digits + string.punctuation
    #options character and english word is stored as a pair in a tuple. # of pairs has the default set to 4. Passing a numarical parameter will update that default setting.
    base_elements = [*zip(random.choices(options, k=length), random.choices(english_words, k=length))]
    #combines each tuple pairs to form a list of each option-character/word combo. 
    group_elements = [*map(''.join, base_elements)]
    #joins all elements of the list into a single string. 
    combine_elements = ''.join(group_elements)
    print(combine_elements)
    
    




RandPassPhrase()

#chars = english_words + string.digits + '!@#$%^&*()'

#x = chars[ord(os.urandom(1)) % len(chars)]


'''
def randPhrase(length=4):
    with open('C:/Python38/word_lists/english_words_dict/english_words.txt', 'r') as f:
        english_words = [line.strip() for line in f]
    f.close()
    print(type(english_words))
    options = string.digits + string.punctuation
    
    x = random.choice(options).join(random.choices(english_words, k=length))
    print(x)

'''
