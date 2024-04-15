

def discrete_logarithm(a, b, m):
    c = 1
    
    while pow(b, c) % m != a:
        c = c + 1
        
    return c

def modular_exponentiation(b, c, m):
    return pow(b, c) % m


if __name__ == '__main__':
    print(modular_exponentiation(5, 948603, 9048610007))
    print(discrete_logarithm(36689093056, 5, 9048610007))