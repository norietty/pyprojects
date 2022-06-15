"""
This script will encrypt a text using the fence rail 
"""

#Getting user input 

plaintext = input('Enter your message to be encrypted please:')

plaintext = plaintext.replace(' ', '').upper()
print(plaintext)

def encrypt(plaintext):
    """
    This function will encrypt the plain text using the rail fence cipher

    Arguments : plaintext

    Returns: The encrpted text
    """
    # encrypt the message using rail fence cipher.
    text_length = len(plaintext)

    encrypted_text = ''
    up_letters = ''
    down_letters = ''

    if text_length % 2 == 0:
        for i in range(text_length):
            if i % 2 == 0:
                up_letters += plaintext[i]
            else:
                down_letters += plaintext[i]
        encrypted_text = up_letters + down_letters
    else:
        first_l = plaintext[-1]
        plaintext = plaintext[::-1]
        for i in range(len(plaintext)):
            if i % 2 == 0:
                up_letters += plaintext[i]
            else:
                down_letters += plaintext[i]
        encrypted_text = first_l + up_letters + down_letters
    # Reconstruct the message using five word-letters
    encrypted_message = ''
    i = 0
    while i  <= len(encrypted_text):
        encrypted_message += encrypted_text[i:i+5] + ' '
        i += 5
    if i % 5 != 0:
        encrypted_message += encrypted_text[-i%5:]
    return encrypted_message


encrypted_message = encrypt(plaintext)
print(f'Here is your encrypted message {encrypted_message}')