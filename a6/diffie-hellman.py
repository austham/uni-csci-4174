"""
CSCI4171: Assignment 6
This program implements the Diffie-Hellman key exchange algorithm.
@Author: Austin Hamel B00824779

"""

import random
import math


def is_prime(n: int):

    if n == 2:
        return True     # 2 is prime

    if n < 2 or n % 2 == 0:
        return False    # 0, 1, negative numbers, and even numbers are not prime

    # check odd numbers up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


def diffie_hellman_exchange(p: int, g: int):
    # ensure p is prime
    if not is_prime(p):
        raise ValueError("p must be prime")

    # Alice picks a secret number between 1 and p-1
    sa = random.randint(1, p - 1)
    print("Chose SA: ", sa)

    # Bob picks a secret number between 1 and p-1
    sb = random.randint(1, p - 1)
    print("Chose SB: ", sb)

    # TA = g^a mod p
    ta = pow(g, sa, p)
    print("TA: ", ta)

    # TB = g^b mod p
    tb = pow(g, sb, p)
    print("TB: ", tb)

    # calculate the shared secret key
    key1 = pow(tb, sa, p)
    key2 = pow(ta, sb, p)
    print("Secret key: ", key1)
    print("Keys match: ", key1 == key2)


def main():
    p, g = [int(c) for c in input("Enter two numbers \"p g\": ").split(" ")]
    diffie_hellman_exchange(p, g)


if __name__ == '__main__':
    main()
