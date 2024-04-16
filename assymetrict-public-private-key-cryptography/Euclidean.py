

def gcd(a, b):
    if a % b == 0:
        return b
    
    return gcd(b, a % b)

def gcd_iter(a, b):
     while a % b != 0:
        a, b = b, a % b
     return b

if __name__ == '__main__':
    # print(gcd(48, 18))
    # print(gcd(24, 9))
    print(gcd_iter(2455, 3965))