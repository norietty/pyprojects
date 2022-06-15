"""
A script to dycrept the route cipher using brute force attack

Required input: an encrypted text, a key, # of column, # of rows.

Prints translated taxt in plain text.
"""

from itertools import combinations, permutations
import sys


#User input 

rows = int(input('Enter the number of rows:'))
cols = int(input('Enter the number of columns:'))
in_key = list(range(1, cols + 1)) + [-i for i in range(1, cols + 1)]
in_key = [list(e) for  e in combinations(in_key, 4)]
def is_column_nd(l):
    for i in l:
        if i in l and -i in l:
            return False
    return True
in_key = [e for e in in_key if is_column_nd(e)]
in_key = [permutations(e) for e in in_key]
in_key1 = []
for e in in_key:
    for l in list(e):
        in_key1.append(l)
print(in_key1)

cipher_text = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

# End of getting  user input 


#Here the main function  which will run the program 
def main():
    """
    Run the program and print plaintext
    """

    
    for key in in_key1:
        print(f"\nCiphertext = {cipher_text}")
        print(f"Trying {cols} columns")
        print(f"Trying {rows} rows")
        print(f"Trying {key}")

        cipherlist = list(cipher_text.split(' '))
        validate_col_row(cipherlist)
        key_int = key_to_int(key)
        translation_matrix = build_matrix(key_int, cipherlist)
        plaintext = decrypt(translation_matrix)
        print(f'plaintext {plaintext}')


def validate_col_row(cipherlist):
    """
    Check that input rows & cols are valid against message length
    """
    factors = []
    len_cipher = len(cipherlist)
    for i in range(2, len_cipher):
        if len_cipher % i == 0:
            factors.append(i)
    print(f"\nLength of cipher is {len_cipher}")
    print(f"Acceptable column/row values are {factors}")

    if rows*cols != len_cipher:
        print("\nError rows & cols not factors of length of cipher terminating program.", file=sys.stderr)
        sys.exit()

def key_to_int(key):
    """
    Turn key into list of integers and check validity.
    """
    key_int = []
    i = 0
    while i < len(key):
        if key[i] == '-':
            key_int.append(-int(key[i+1]))
            i += 2
        else:
            key_int.append(int(key[i]))
            i += 1
        
    key_int_lo = min(key_int)
    key_int_hi = max(key_int)
    if len(key_int) != cols or key_int_lo < -cols or key_int_hi > cols or 0 in key_int:
        print("\nError Problem with the key Terminating", file=sys.stderr)
        sys.exit()
    else:
        return key_int

def build_matrix(key_int, cipherlist):
    """
    Turn every n item in cipher list into a new item in a list of lists.
    """

    translation_matrix = [None]*cols
    start = 0
    stop = rows
    for k in key_int:
        if k < 0:
            col_item = cipherlist[start:stop]
        else:
            col_item = list(reversed(cipherlist[start:stop]))
        translation_matrix[abs(k) -1] = col_item
        start += rows
        stop += rows
    return translation_matrix

def decrypt(translation_matrix):
    """
    Loop through nested lists popping of last item of a string 
    """
    plaintext = ''
    for i in range(rows):
        for matrix_col in translation_matrix:
            word = str(matrix_col.pop())
            plaintext += word + ' '
    return plaintext


if __name__=="__main__":
    main()
