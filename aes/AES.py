# Adavanced Encryption Standard
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Private key
key = get_random_bytes(16)
# key2 = b'Not sixteen byte key'

print(key)
# print(key2)
cipher = AES.new(key, AES.MODE_CBC)
print(cipher.iv)
print(cipher.block_size)

plaintext = b'This is a message!'
print(pad(plaintext, AES.block_size))

ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
iv = cipher.iv

decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
original_text = unpad(decrypt_cipher.decrypt(ciphertext), AES.block_size)

print(original_text.decode())