"""
Load a text file as a list

Arguments: A text file 

Retuerns: a list of word 

Execptions: An error execption if file not found 

Requiers import sys
"""
import sys

def load(file):
    """
    Open a text file and returns a list of words 
    """

    try:
        with open(file, 'r') as f:
            words = f.read().strip().split('\n')
            words = [word.lower() for word in words]
        return words
    except IOError as e:
        print(f'{e} Error opening {f}. Terminaiting program.', file=sys.stderr)
        sys.exit(1)

