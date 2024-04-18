from hashlib import md5

s = 'Achilles and Flocka'

result = md5(s.encode())
print(result.hexdigest())