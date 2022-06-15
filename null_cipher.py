"""
This script will implement the null cipher which will the user choose the letter will be used.
"""

from load_dictionary import load
##-----------------------------------------------------
#USER INPUT 

letter_num = int(input('Enter the number of a  letter after a punctiation mark:'))

ciphertext = load('travnion.txt')
ciphertext = ''.join(ciphertext)
#print(cipertext)

#End Of user input ------------------------------------------------

def main():
    'This function will Run the program and print the hidden message'
    global ciphertext
    ciphertext = ''.join(ciphertext.split(' '))
    print(f'\nCiphertext is {ciphertext}')
    message = hidden_msg(ciphertext )
    print(f'The message is {message}')

def find_nth_l(n, word):
   if word[:n].isalpha():
    return word[:n][-1]

def hidden_msg(ciphertext):
    msg = ''
    for i in range(len(ciphertext)):
        if ciphertext[i] in '.:;,\'' and find_nth_l(letter_num, ciphertext[i+1:]):
            msg += find_nth_l(letter_num, ciphertext[i+1:])
    return msg
            
if __name__=="__main__":
    main()

