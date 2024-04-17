

def modular_inverse(a, m):
    for inv in range(0, m):
        if (a * inv) % m == 1:
            return inv
        
    print('There is no modular inverse for', a, 'modulo', m)
    

if __name__ == '__main__':
    print(modular_inverse(9, 31))