"""
CSCI4171: Assignment 5
This program implements the RSA algorithm for encryption and decryption.
@Author: Austin Hamel B00824779

"""


# function to check if a number is prime for error checking
def is_prime(a):
    return any([i for i in range(2, a) if a % i == 0])


# function to calculate the greatest common divisor of two numbers using euclidian algorithm
def gcd_euclidian(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# function to find rsa keys using the prime numbers p and q
def rsa_get_keys(p, q):

    # check if p and q are prime
    if is_prime(p) or is_prime(q):
        raise ValueError("p and q must be prime numbers.")

    n = p * q
    foo = (p - 1) * (q - 1)

    # choose an integer e that is relatively prime to (p-1)(q-1)
    e = 2
    while (gcd_euclidian(e, foo) != 1):
        e += 1

    # find an integer d such that (e * d)mod(p-1)(q-1) = 1
    d = 1
    while (e * d) % foo != 1:
        d += 1

    pub_key = [e, n]
    priv_key = [d, n]
    return pub_key, priv_key


# function to encrypt a message m using the public key
def rsa_encrypt(pub_key, m):
    e, n = pub_key

    # break up the exponent calculation into squares to avoid overflow
    c = 1
    for i in range(e):
        c = (c * m) % n
    return c


# function to decrypt a message c using the private key
def rsa_decrypt(priv_key, c):
    d, n = priv_key

    # break up the exponent calculation into squares to avoid overflow
    m = 1
    for i in range(d):
        m = (m * c) % n
    return m


# main function
def main():
    p, q = (input("Enter the prime numbers, p and q: ").split())
    p, q = int(p), int(q)

    print("Calculating RSA values...")
    pub_key, priv_key = rsa_get_keys(p, q)
    print("Public RSA key is:", pub_key, "\nPrivate RSA key is:", priv_key)

    m = input("Enter the plaintext message m (an integer): ")
    m = int(m)

    print("Encrypting m...")
    c = rsa_encrypt(pub_key, m)
    print("The ciphertext c is:", c)

    print("Decrypting c...")
    m = rsa_decrypt(priv_key, c)
    print("The plaintext m is:", m)


# invoke main function
if __name__ == "__main__":
    main()
