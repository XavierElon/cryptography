import matplotlib.pylab as plt

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
    
if __name__ == '__main__':
    plain_text = 'In this course you will learn about cryptography and hashing in Python and Java as well. You will understand most of the private key (symmetric) and pubic key (asymmetric) cryptosystems on a step by step basis. You can learn about the theory as well as the implementation for every cryptographic algorithm - and how to crack these systems (so what are the weaknesses).'
    freq = frequency_analysis(plain_text)
    plot_distribution(freq)