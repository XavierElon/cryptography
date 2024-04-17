import random
from math import floor, sqrt

RANDOM_START = 1e3
RANDOM_END = 1e5

def is_prime(num):
    if num < 2:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, floor(sqrt(num))):
        if num % i == 0:
            return False
        
    return True