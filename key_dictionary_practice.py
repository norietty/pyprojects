"""
This script will take a key and store as a dictionary.
"""

#---------------------------------------
#USER INPUT 

key = input('Enter your key please:')

#--------------------------------------

def build_key_dict(key):
    """
    This function will build a dict foe the key
    """
    keylist = []
    i = 0
    while i < len(key):
        if key[i] == '-':
            keylist.append(-int(key[i+1]))
            i += 2
        else:
            keylist.append(int(key[i]))
            i += 1
    key_dict = {}
    for k in keylist:
        if k < 0:
            key_dict[k] = 'up'
        else:
            key_dict[k] = 'down'
    return key_dict

key_dict = build_key_dict(key)
print(f'The key as dictionary is: {key_dict}')
