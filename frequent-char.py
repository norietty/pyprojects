"""
A simple programm to print a bar chart of charchter in a sentence.
"""

import pprint

def main():
    """
    A function to print a bar chart of charcheters in a sentence.

    arg: Take input form th command line 

    print: a bar chart 
    """

    while True:

        sentence = input("Enter your sentence or press n to exit: ")

        if sentence == 'n':
            break

        char_dic = {}
        alphabet = 'qwertzuioplkjhgfdsamnbvcxy'
        for ch in alphabet:
            char_dic[ch] = []
        for ch in sentence:
            ch = ch.lower()
            if not ch.isalpha():
                continue
            if ch in char_dic:
                char_dic[ch] = char_dic[ch] + [ch]

            else:
                char_dic[ch] = [ch]

        for elm in char_dic:
            print(f'{elm}: {char_dic[elm]}')

if __name__=="__main__":
    main()

        
