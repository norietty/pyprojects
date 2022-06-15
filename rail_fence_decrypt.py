"""
This Script will decrypt a message encrepted with 2 fence rails.
"""

#USER INPUT

encrypted_msg = input('Enter your message to be decrypted please:')

#---------------


#The main functions 

def main():
    """Run the program and print the decrypted message."""
    message = prep_message(encrypted_msg)
    rails = build_rails(message)
    dycrept(rails)


def prep_message(encrypted_msg):
    """Remove white spaces from the message """
    encrypted_msg = encrypted_msg.replace(' ', '').upper()
    print(f'\nThe encrypted message is {encrypted_msg}')
    return encrypted_msg

def build_rails(message):
    """Divide the message to two chunks to be encrypted."""
    length_msg = len(message)
    first_rails = message[:length_msg//2]
    last_rails = message[length_msg//2:]
    return first_rails, last_rails

def dycrept(rails):
    """This function will reconstruct the message for the chunks"""
    message = ''
    for i in range(len(rails[0])):
        message += rails[0][i]
        message += rails[1][i]
    if len(rails[0]) < len(rails[1]):
        message += rails[1][-1]
    print(f'\nThe decrypted message is: {message}')


if __name__=="__main__":
    main()