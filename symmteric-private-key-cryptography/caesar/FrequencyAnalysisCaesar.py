import matplotlib.pylab as plt

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
KEY = 8

def caesar_encrypt(plain_text):
    cipher_text = ''
    plain_text = plain_text.upper()
    for c in plain_text:
        index = LETTERS.find(c)
        
        index = (index + KEY) % len(LETTERS)
        cipher_text = cipher_text + LETTERS[index]
        
    return cipher_text

def frequency_analysis(text):
    text = text.upper()
    
    letter_frequencies = {}
    
    for letter in LETTERS:
        letter_frequencies[letter] = 0
        
    for letter in text:
        if letter in LETTERS:
            letter_frequencies[letter] += 1
    
    return letter_frequencies

def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values(), color='g', width=0.5)
    plt.show()
    
def caesar_crack(cipher_text):
    freq = frequency_analysis(cipher_text)
    print(freq)
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print(freq)
    print("The possible key value: %s" % (LETTERS.find(freq[0][0]) - LETTERS.find('E')))
    
if __name__ == '__main__':
    plain_text = 'In this course you will learn about cryptography and hashing in Python and Java as well. You will understand most of the private key (symmetric) and pubic key (asymmetric) cryptosystems on a step by step basis. You can learn about the theory as well as the implementation for every cryptographic algorithm - and how to crack these systems (so what are the weaknesses).'
    cipher_text = caesar_encrypt(plain_text)
    print(cipher_text)
    # freq = frequency_analysis(cipher_text)
    caesar_crack(cipher_text)
    # plot_distribution(freq)