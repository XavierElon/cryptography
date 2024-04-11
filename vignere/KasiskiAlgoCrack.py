import collections
import math

def find_repeats(text, gap_min=3):
    """ Find repeated sequences of characters in a text. """
    sequences = collections.defaultdict(list)
    for i in range(len(text) - gap_min + 1):
        seq = text[i:i + gap_min]
        sequences[seq].append(i)
    return {seq: pos for seq, pos in sequences.items() if len(pos) > 1}

def calculate_distances(repeats):
    """ Calculate the distances between repeated sequences. """
    distances = []
    for positions in repeats.values():
        for i in range(len(positions) - 1):
            distances.append(positions[i + 1] - positions[i])
    return distances

def gcd_of_distances(distances):
    """ Calculate the GCD of a list of distances. """
    gcd = distances[0]
    for distance in distances[1:]:
        gcd = math.gcd(gcd, distance)
    return gcd

def kasiski_examination(ciphertext):
    """ Perform Kasiski Examination to suggest the key length. """
    repeats = find_repeats(ciphertext)
    distances = calculate_distances(repeats)
    if not distances:
        return None
    return gcd_of_distances(distances)


def frequency_analysis(text):
    """ Return the frequency of each letter in the text. """
    frequencies = collections.Counter(text)
    total = len(text)
    return {char: freq / total for char, freq in frequencies.items()}

def chi_squared(observed, expected):
    """ Calculate the Chi-squared statistic for observed and expected frequencies. """
    return sum((observed.get(chr(i + ord('A')), 0) - expected[chr(i + ord('A'))]) ** 2 / expected[chr(i + ord('A'))] for i in range(26))

def find_key(ciphertext, key_length):
    """ Determine the key using frequency analysis. """
    # English letter frequency (approximation)
    english_freq = {'E': 12.02, 'T': 9.10, 'A': 8.12, 'O': 7.68, 'I': 7.31, 'N': 6.95, 'S': 6.28, 'R': 6.02,
                    'H': 5.92, 'D': 4.32, 'L': 3.98, 'U': 2.88, 'C': 2.71, 'M': 2.61, 'F': 2.30, 'Y': 2.11,
                    'W': 2.09, 'G': 2.03, 'P': 1.82, 'B': 1.49, 'V': 1.11, 'K': 0.69, 'X': 0.17, 'Q': 0.11, 'J': 0.10, 'Z': 0.07}
    # Normalize English frequencies
    total = sum(english_freq.values())
    english_freq = {k: v / total for k, v in english_freq.items()}

    key = ''
    for i in range(key_length):
        # Get the ith subtext
        subtext = ciphertext[i::key_length]
        observed_freq = frequency_analysis(subtext)
        min_chi_sq = float('inf')
        likely_shift = 0
        # Try all possible shifts for this part of the key
        for shift in range(26):
            shifted_freq = {chr((ord(char) - ord('A') - shift) % 26 + ord('A')): freq for char, freq in observed_freq.items()}
            chi_sq = chi_squared(shifted_freq, english_freq)
            if chi_sq < min_chi_sq:
                min_chi_sq = chi_sq
                likely_shift = shift
        # Determine the most likely letter in the key
        key += chr(ord('A') + likely_shift)
    return key

def decrypt_vigenere(ciphertext, key):
    """ Decrypt the Vigenère cipher using a given key. """
    key_length = len(key)
    plaintext = []

    # Convert ciphertext to numbers: A=0, B=1, ..., Z=25
    ciphertext_nums = [ord(char) - ord('A') for char in ciphertext]
    # Convert key to numbers: A=0, B=1, ..., Z=25
    key_nums = [ord(char) - ord('A') for char in key]

    # Decrypt each character
    for i in range(len(ciphertext)):
        # Apply Vigenère decryption formula
        n = (ciphertext_nums[i] - key_nums[i % key_length] + 26) % 26
        # Convert number back to letter
        plaintext.append(chr(n + ord('A')))

    # Join list into string
    return ''.join(plaintext)


if __name__ == "__main__":
    ciphertext = "VHVSSPQUCEMRVBVBBBVHVSURQGIBDUGRNICJQUCERVUAXSSR"
    # ciphertext = 'IORFNDBCFRVPRBCDFKLOOHVCDQGCPLFKHOOH'
    key_length = kasiski_examination(ciphertext)
    key = find_key(ciphertext, key_length)
    print(f"Suggested key length is: {key_length}")
    print(f"Suggested key is: {key}")
    plaintext = decrypt_vigenere(ciphertext, "LEMON")
    print(f"Decrypted text is: {plaintext}")