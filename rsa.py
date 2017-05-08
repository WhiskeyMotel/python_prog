import random

##проверить, является ли  число простым
def is_prime(n):
    ##делаем цикл от 2 до числа, предшествующего проверяемому
    for i in range (2,n-1):
        if n%i==0: ##если число делится без остатка,
            return 'False' ##то мы возвращаем False, то есть оно сложное
            break
    return 'True' ##если нет такого делителя, то возвращаем True, то есть число делится только на 1 и само себя

def gcd(a, b):
    """
    Euclid's algorithm for determining the greatest common divisor.

    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while a != b:
        if a>b:
            a = a-b
        else:
            b=b-a
    return a


def sub_help(e, phi):
    if phi == 0:
        return e,1,0
    else:
        d,x,y = sub_help(phi, e%phi)
        return d,y,x-y*(e//phi)

def multiplicative_inverse(e, phi):
    """
    Euclid's extended algorithm for finding the multiplicative
    inverse of two numbers.

    >>> multiplicative_inverse(7, 40)
    23
    """
    d,x,y = sub_help(e, phi)
    return x%phi

def generate_keypair(p, q):
    if is_prime(p)=='False' or is_prime(q)=='False':
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    # n = pq
    n = p*q

    # phi = (p-1)(q-1)
    phi = (p-1)*(q-1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    # Unpack the key into it's components
    key, n = pk
    # Convert each letter in the plaintext to numbers based on
    # the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]
    # Return the array of bytes
    return cipher


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    # Return the array of bytes as a string
    return ''.join(plain)


if __name__ == '__main__':
    print("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")
    encrypted_msg = encrypt(private, message)
    print("Your encrypted message is: ")
    print(''.join(map(lambda x: str(x), encrypted_msg)))
    print("Decrypting message with public key ", public, " . . .")
    print("Your message is:")
    print(decrypt(public, encrypted_msg))
