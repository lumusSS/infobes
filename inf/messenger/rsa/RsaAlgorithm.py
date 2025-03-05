import random
import math

KEYS_LENGTH = 32

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_candidate(length):
    p = random.getrandbits(length)

    p |= (1 << length - 1) | 1
    return p
    

def generate_prime_number(length=8):
    p = generate_prime_candidate(length)
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p
    
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('Обратный элемент по модулю не существует')
    return x % m
    

class RSA:
    def __init__(self):
        
        self.p = generate_prime_number(KEYS_LENGTH)
        self.q = generate_prime_number(KEYS_LENGTH)
        
        while self.q == self.p:
            self.q = generate_prime_number(KEYS_LENGTH)
    
        n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)

        # Выбираем стандартное значение для e
        e = 65537
        if math.gcd(e, phi) != 1:
            # Если 65537 не подходит, подбираем другое e
            e = 3
            while math.gcd(e, phi) != 1:
                e += 2

        d = modinv(e, phi)
        
        self.public_key = e
        self.private_key = d
