

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = egcd(a % b, a)
    
    x = y1 - (b // a) * x1
    y = x1