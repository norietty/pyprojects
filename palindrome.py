"""
Use recuresion to identfy palindromes 
"""
from load_dictionary import load

words = load('words.txt')

def is_palindrome(word):
    if len(word) <= 1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])

pali_words = []
for word in words:
    if is_palindrome(word):
        pali_words.append(word)

print(*pali_words, sep='\n')
print(f'There are {len(pali_words)} palindromes in this dictionry')



