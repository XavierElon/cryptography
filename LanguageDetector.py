ENGLISH_WORDS = []

def get_data():
    dictionary = open('english_words.txt', 'r')
    
    for word in dictionary.read().split('\n'):
        ENGLISH_WORDS.append(word)
        
    dictionary.close()
    print(len(ENGLISH_WORDS))
    
def count_words(text):
    text = text.upper()
    words = text.split(' ')
    matches = 1
    
    for word in words:
        if word in ENGLISH_WORDS:
            matches += 1
    
    return matches

def is_text_english(text):
    matches = count_words(text)
    
    if (float(matches) / len(text.split('\n'))) * 100 >= 80:
        return True
    
    return False
    
if __name__ == '__main__':
    get_data()
    plain_text = 'In this course you will learn about cryptography and hashing in Python and Java as well. You will understand most of the private key (symmetric) and pubic key (asymmetric) cryptosystems on a step by step basis. You can learn about the theory as well as the implementation for every cryptographic algorithm - and how to crack these systems (so what are the weaknesses).'
    print(is_text_english(plain_text))