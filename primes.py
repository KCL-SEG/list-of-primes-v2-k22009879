"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    base = 2
    list = []
    if  number_of_primes <1:
        raise ValueError("number must be greater than 0")

    if number_of_primes == 1:
        list.append(base)
        return list
    else:
        list.append(base)
        while len(list)<number_of_primes:

            base = base+1
            if isPrime(base):
                list.append(base)
    print(list)




    return list

def isPrime(num):
    if num ==1:
        return False
    elif num > 1:
        for i in range (2, num):
            if num%i == 0:
                return False
    return True
