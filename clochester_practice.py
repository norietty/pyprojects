"""This script will hide a message using the nth charachter of every nth word
"""

from load_dictionary import load
import string

#-----------------------------------------------------------------------
#USER INPUT 

char_num = int(input('Enter the cherachter index to be used: '))

ciphertext = load('clochester_message.txt')


####-----------------------------------

def main():
    """This function will run the program and print the message."""
    global ciphertext
    print(f'\nThe original message is {ciphertext}')
    ciphertext = ciphertext[0].split(' ')
    h_message = find_message(ciphertext, char_num)
    print(f'The hidden message is {h_message}')

def find_message(ciphertext, char_num):
    """This function will find the message using nth char after every nth word"""

    message = ''
    i = 0
    while i < len(ciphertext):
        if len(ciphertext[i]) > char_num - 1:
            if ciphertext[i][char_num] in string.ascii_lowercase:
                message += ciphertext[i][char_num - 1]
        i += char_num
    return message

if __name__=="__main__":
    main()
