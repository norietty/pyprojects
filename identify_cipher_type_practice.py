"""
Identify cipher type 
"""
from collections import Counter
from load_dictionary import load
#-----------------------------------
#USER INPUT
ciphertext = input('Enter your text please:')


#------------------------------------------

ciphertext = ''.join(ciphertext.split(' '))
ciphertext = ciphertext.upper()





englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

def build_freq(ciphertext):
    freq = Counter(ciphertext)
    for key in freq.keys():
        freq[key] = (freq[key]/len(ciphertext))*100
    return freq

def cipher_type(freq, englishfreq):
    """
    Identify if the cipher used transposition or substution
    """
    delta = 0
    for l in freq:
        delta += abs(freq[l] -  englishfreq[l])
    print(delta)
    if delta > 20:
        print('This is a substition cpher')
    else:
        print('This is a transposition cipher')


freq = build_freq(ciphertext)


cipher_type(freq, englishLetterFreq)




