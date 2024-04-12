from random import randint

ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(text, key):
    text = text.upper()
    cipher_text = ''
    
    for index, char in enumerate(text):
        key_index = key[index]
        
        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]
        
    return cipher_text

def decrypt(cipher, key):
    plain = ''
    
    for index, char in enumerate(cipher):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain += ALPHABET[(char_index - key_index) % len(ALPHABET)]
        
    return plain
        

def random_sequence(text):
    random = []
    
    for _ in range(len(text)):
        random.append(randint(0, len(ALPHABET)))
        
    return random

if __name__ == '__main__':
    
    message = 'In this course you will learn about cryptography and hashing in Python and Java as well. You will understand most of the private key (symmetric) and pubic key (asymmetric) cryptosystems on a step by step basis. You can learn about the theory as well as the implementation for every cryptographic algorithm - and how to crack these systems (so what are the weaknesses).'
    seq = random_sequence(message)
    print("Original message: %s" % message.upper())
    cipher_text = encrypt(message, seq)
    print("Encrypted message: %s" % cipher_text)
    decrypted_text = decrypt(cipher_text, seq)
    print("Decrypted message: %s" % decrypted_text)