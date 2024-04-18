from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


key = RSA.generate(2048)
private_key = key
public_key = key.public_key()

# file = open("mykey.pem", "wb")
# file.write(key.export_key())

data = "Flocka".encode()
session_key = get_random_bytes(16)
encrypt_rsa = PKCS1_OAEP.new(public_key)
enc_session_key = encrypt_rsa.encrypt(session_key)

cipher_aes = AES.new(session_key, AES.MODE_GCM)
cipher_text, tag = cipher_aes.encrypt_and_digest(data)

nonce = cipher_aes.nonce

print('ciphertext %s ' % cipher_text)
print('tag %s ' % tag)

decrypt_rsa = PKCS1_OAEP.new(private_key)
sess_key = decrypt_rsa.decrpyt(enc_session_key)

decrypt_aes = AES.new(sess_key, AES.MODE_GCM, nonce)
plain_text = decrypt_aes.decrpyt_and_verify(cipher_text, tag)

print(plain_text.decode())