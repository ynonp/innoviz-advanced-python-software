from math import *

def is_prime(n: int) -> bool:
    for candidate in range(2, int(ceil(sqrt(n))) + 1):
        if n % candidate == 0:
            return False
    return True

def count_primes(start, end):
    res = 0
    for i in range(start, end):
        if is_prime(i):
            res += 1

    return res

print(count_primes(1, 1_000_000))

# Your Task:
# Run count_primes in multiple threads (2 threads, 4 threads)
# And check if it found the result faster and was still accurate
