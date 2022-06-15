"""
A programm to generate bic latin word 
"""

import sys 

def main():
    """
    Will generate some big word 

    args: A word 

    prints: A big latin word 
    """
    while True:
        word =  input("Enter a word or 'n' to quit: ")

        if word == 'n':
            break

        if word[0] in "aieuo":
            word = word + 'way'
            

        else:
            word = word[1:] + word[0] + 'ay'
        
        print(f'{word}', file=sys.stderr)
        print('\n\n')

if __name__=="__main__":
    main()
            
        
        