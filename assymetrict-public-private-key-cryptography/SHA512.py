from hashlib import sha512

s = 'Hello World!'
s1 = 'Hello World#'

result = sha512(s.encode())
result2 = sha512(s1.encode())

print(result.hexdigest())
print(result2.hexdigest())