ALPHABET = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
    matches = 0
    
    for word in words:
        if word in ENGLISH_WORDS:
            matches += 1
    
    return matches

def is_text_english(text):
    matches = count_words(text)
    
    perc = (float(matches) / len(text.split(' '))) * 100
    print('perc = {}'.format(perc))
    
    if perc >= 80:
        return True
    
    return False

def caesar_crack(cipher_text):
    for key in range(len(ALPHABET)):
        plain_text = ''
        
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]
            
        if is_text_english(plain_text):
            print('We have manged to crack Caesar cipher, the key is: %s, the message is : %s' % (key, plain_text))
            
    
if __name__ == '__main__':
    get_data()
    encrypted = 'VJKUBKUBCBOGUUCIG'
    caesar_crack(encrypted)