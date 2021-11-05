
import random
from words import words
import string

def get_word(words):
    word=random.choice(words)
    if '-' in word or ' ' in word:
        get_word(words)
    
    return word.upper()

def hangman():
    lives=5
    word=get_word(words)
    letters_in_word=set(word)
    valid_letters=set(string.ascii_uppercase)
    used_letters=set()

    while not(len(letters_in_word)==0):

        for i in word:
            if i in used_letters:
                print(i,end=" ")
            else:
                print('_',end=" ")

        user_input=input('\n Guess Your Letter \n')
        user_input=user_input.upper()

        if user_input in valid_letters:
            if not(user_input in used_letters):
                used_letters.add(user_input)
                if user_input in letters_in_word:
                    letters_in_word.remove(user_input)
                    if(lives<5):
                        lives+=1
                else:
                    lives-=1
                    print(f'{user_input} is not in the word')
            else:
                print('You have already used that letter')
        else:
            print(f'{user_input} is not a valid letter')
        
        if lives==0:
            break
        print(f'You Have {lives} chances left!')
    if lives==0:
        print(f'You have used all your chances. The answer was : {word}')
    else:
        print(f'You Have Won This Game')

hangman()