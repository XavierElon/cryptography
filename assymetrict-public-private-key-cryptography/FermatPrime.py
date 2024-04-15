import random

def is_prime(n, k=10):
    if n <= 1:
        return False
    
    for _ in range(k):
        a = random.randrange(2, n-1)
        if pow(a, n-1, n) != 1:
            return False
        
    return True


if __name__ == '__main__':
    print(is_prime(10))
    print(is_prime(991948530947555497))