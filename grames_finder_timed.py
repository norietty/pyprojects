"""
This a program to find palingrames in file 
"""
from load_dictionary import load 
import time

start_time = time.time()
words = load('words.txt')
words = [word for word in words if len(word) > 1]
words = set(words)

def is_palindrome(word):
    """
    Arguments: a word 

    Returns: is the word a palindrome or not  
    """
    return word == word[::-1]
    
def find_palingrames():
    grames = []
    for word in words:
        if len(word) > 1:
            for i in range(1, len(word)):
                if word[:i][::-1] in words and is_palindrome(word[i:]):
                    gram = word + ' ' + word[:i][::-1]
                    grames.append(gram)

                if is_palindrome(word[:i]) and word[i:][::-1] in words:
                    gram = word[i:][::-1] + ' ' + word 
                    grames.append(gram)
    return grames

grames = find_palingrames()

print(*grames, sep='\n')
print(f'There are {len(grames)} palingerames in this dictionery')

end_time = time.time()

print(f'This program took about {end_time - start_time} secondes')


