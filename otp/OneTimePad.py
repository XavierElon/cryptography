from random import randint

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(text, key):
    text = text.upper()
    key = key.upper()

def decrypt(text):
    pass

def random_sequence(text):
    random = []
    
    for _ in range(len(text)):
        random.append(randint(0, len(ALPHABET)))
        
    return random

if __name__ == '__main__':
    
    message = 'This is a random text'
    print(random_sequence(message))