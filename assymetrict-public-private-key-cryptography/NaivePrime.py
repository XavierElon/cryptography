from math import sqrt, floor

def is_prime(num):
    if num < 2:
        return False
    
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    
    for n in range(3, floor(sqrt(num)), 2):
        if num % n == 0:
            return False
        
    return True

if __name__ == '__main__':
    print(is_prime(991948530947555497))