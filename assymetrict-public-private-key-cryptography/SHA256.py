from hashlib import sha256

s = 'Hello World!'
s1 = 'Hello World#'

result = sha256(s.encode())
result2 = sha256(s1.encode())

print(result.hexdigest())
print(result2.hexdigest())