"""
This a  model for recognizing anagrams in a dictionary 
"""

from load_dictionary import load

words = load('words.txt')


def find_anagrams(word):
    anagrams = []
    for w in words:
        w = w.lower()
        if sorted(word) == sorted(w) and word != w:
            anagrams.append(w)    
    return anagrams

word = input('Enter a word:')
word = word.lower()
anagrams = find_anagrams(word)

if len(anagrams):
    print(*anagrams, sep='\n')
    print(f'we found {len(anagrams)} anagrams of your word.')
else:
    print('You need a larger dictionary to find anagrams for this word.')


