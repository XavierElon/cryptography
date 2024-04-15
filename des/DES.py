# Data Encryption Standard
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

key = b'mysecret'

cipher = DES.new(key, DES.MODE_ECB)
print(cipher.iv)
print(cipher.block_size)

plaintext = b'This is a message'
ciphertext = cipher.encrpyt(pad(plaintext, DES.block_size))
print(binascii.hexlify(ciphertext))
iv = cipher.iv

decrypt_cipher = DES.new(key, DES.MODE_ECB, iv)
original = decrypt_cipher.decrypt(ciphertext)
original = unpad(original, DES.block_size)
print(original.decode())
