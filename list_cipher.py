"""
This script will implment a list cipher
"""

import sys 
from load_dictionary import load

#--------------------------------------------------
#USER INPUT 

ciphertext = input('\n(Enter your message to e hide: ')
ciphertext = ''.join(ciphertext.split())

l_num = int(input('Enter the letter to be used: '))

#End USER INPUT
#----------------------------------------------------------

#Load an English dictionary to search for words in.

words = load('words.txt')

def main():
    """This function will run the program and print the result"""
    print(f'\nThe length of the message is {len(ciphertext)}')
    print(f'The actual message is {len(ciphertext)}')
    list_words = find_word_list(ciphertext, words, l_num)
    print(f'You can hide your message in this list {list_words}')

def find_word_list(ciphertext, words, l_num):
    """This function will find words that will be used to hide the message."""
    words_msg = []
    for l in ciphertext:
        for word in words:
            if len(word) >= l_num and l in word:
                if word.index(l)  == l_num - 1:
                    words_msg.append(word)
                    break

    print(f'Number of word found {len(words_msg)}')
    return words_msg


if __name__=='__main__':
    main()