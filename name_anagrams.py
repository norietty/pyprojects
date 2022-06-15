"""
This a program to build a phrase anagram to a given name 

"""


from load_dictionary import load 

from collections import Counter

words = load('words.txt')

name = input('Enter your name please:').lower()
phrase = []
leftovers = name

def word_in_name(word, name):
    """
    A function to detemine if all letters in word are in a name

    Arg: a word

    Return:True or False
    """

    dict_name = Counter(name.lower())
    dict_word = Counter(word.lower())

    if len(dict_word) > len(dict_name):
        return False

    for key in dict_word.keys():
        if key not in dict_name.keys():
            return False
        if dict_word[key] > dict_name[key]:
            return False
    return True

def find_anagrams(name):
    word_list = []
    for word in words:
        if word_in_name(word, name):
            word_list.append(word)
    return word_list

def length(l):
    n = 0
    for w in l:
        n += len(w)
    return n

def extract_choice(choice, leftovers):
    left = ''
    for key in Counter(leftovers):
        left += (Counter(leftovers)[key] - Counter(choice)[key])*key
    return left

def process_choice():
    choice = input('Make a choice or start over:')
    if choice:
        if choice in find_anagrams(leftovers):
            leftover = extract_choice(choice, leftovers)
            return choice, leftover
        else:
            process_choice()

def main():
    """
    This function handle the mian logique in the programm.
    """
    global leftovers
    while length(phrase) < len(name):
        anagrams_list = find_anagrams(leftovers)
        print(f'We found {len(anagrams_list)} of your name in our dict:')
        print(*anagrams_list, sep='\n')
        choice = process_choice()
        if choice:
            phrase.append(choice[0])
            leftovers = choice[1]
            print(phrase, leftovers)
    name_anagram = ''
    for word in phrase:
        name_anagram += word + ' '
    print(f'Here is the anagram phrase of your name: {name_anagram}')



if __name__=="__main__":
    main()

    
   







