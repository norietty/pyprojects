"""
This script will hide a message to save queen mary using a list of famliy names.
"""

from load_dictionary import load

from random import randint
##########------------------------------------------

message = 'Give your word and we rise'
message = ''.join(message.split()).lower()

names = load('supporters.txt')

#------------------------------------------------------

def main():
    """This function will run the program and print the list names"""
    #print(find_name(1, names, 'g'))
    print(f'\nThe original message is {message}')
    supporters = build_list(names, message)
    supporters.insert(2, 'Jacob')
    supporters.insert(5, 'Stuart')
    print('Here your majesty you\'ll find a list who support you.')
    print(*supporters, sep='\n')

def find_name(ind, names, char):
    """This function will find a name toe hide the charcheter in."""

    for name in names:
        if name[ind] == char:
            break
    return name

def build_list(names, message):
    """This function will find the names will be used to hide the message."""

    list_names = []
    while len(list_names) < len(message):
        for char in message:
            names1 = list(set(names) - set(list_names))
            if len(list_names) % 2 == 0:
                list_names.append(find_name(1, names1, char))
            else:
                list_names.append(find_name(2, names1, char))
    return list_names


if __name__=="__main__":
    main()


