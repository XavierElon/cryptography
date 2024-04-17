

def egcd(a, b):
    """
    Computes the greatest common divisor (GCD) of two integers `a` and `b` using the Extended Euclidean algorithm.
    
    The Extended Euclidean algorithm also computes the coefficients `x` and `y` such that `a * x + b * y = gcd(a, b)`.
    
    This function is typically used in cryptography to compute modular inverses, which are required for RSA and other public-key cryptography algorithms.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    
    Returns:
        Tuple[int, int, int]: A tuple containing the GCD of `a` and `b`, and the coefficients `x` and `y` such that `a * x + b * y = gcd(a, b)`.
    """
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = egcd(b % a, a)
    
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y
    

"""
Computes the greatest common divisor (GCD) of two integers `a` and `b` using the Extended Euclidean algorithm.

The Extended Euclidean algorithm also computes the coefficients `x` and `y` such that `a * x + b * y = gcd(a, b)`.

This function is typically used in cryptography to compute modular inverses, which are required for RSA and other public-key cryptography algorithms.

Args:
    a (int): The first integer.
    b (int): The second integer.

Returns:
    Tuple[int, int, int]: A tuple containing the GCD of `a` and `b`, and the coefficients `x` and `y` such that `a * x + b * y = gcd(a, b)`.
"""
if __name__ == '__main__':
    print(egcd(15, 56))
    print(egcd(7, 9))