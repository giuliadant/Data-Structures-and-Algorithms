import math

#prime checker
def prime_checker(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    #check odd divisors up to square root
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

#sieve of eratosthenes
def sieve_of_eratosthenes(n):
    if n < 2:
        print("No primes exist below 2.")
        return []
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for p in range(2, int(math.sqrt(n)) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False

    primes = [i for i in range(2, n + 1) if prime[i]]
    print(f"Prime numbers up to {n}: {primes}")
    return primes

n = int(input("Enter a number: "))

print(f"Is {n} a prime number? {prime_checker(n)}")

primes_up_to_n = sieve_of_eratosthenes(n)

#verify all primes from the sieve using prime_checker
if primes_up_to_n:  #check if the list is not empty
    all_verified = all(prime_checker(p) for p in primes_up_to_n)
    print(f"All primes from sieve verified by prime checker: {all_verified}")
else:
    print("No primes to verify.")