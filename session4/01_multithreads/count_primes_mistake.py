from math import *
import threading, time

"""
Coffee break until 12:20
Please download this folder from git:

https://github.com/ynonp/innoviz-advanced-python-software/tree/main/session4/c_extensions
"""


"""
Your Task:
Run count_primes in multiple threads (2 threads, 4 threads)
And check if it found the result faster and was still accurate

All files are in github:
http://github.com/ynonp/innoviz-advanced-python-software 
"""

result = 0


def is_prime(n: int) -> bool:
    for candidate in range(2, int(ceil(sqrt(n))) + 1):
        if n % candidate == 0:
            return False
    return True


def count_primes(start, end):
    global result
    for i in range(start, end):
        if is_prime(i):
            result += 1

    return result

print("Count Primes (single)")
s0 = time.time()
print(count_primes(1, 1_000_000))
s1 = time.time()
print(f"Took {s1 - s0} ms")

result = 0
w1 = threading.Thread(target=count_primes, args=(1, 250_000))
w2 = threading.Thread(target=count_primes, args=(250_000, 500_000))
w3 = threading.Thread(target=count_primes, args=(500_000, 750_000))
w4 = threading.Thread(target=count_primes, args=(750_000, 1_000_000))

for w in [w1, w2, w3, w4]:
    w.start()

for w in [w1, w2, w3, w4]:
    w.join()

print(result)
s1 = time.time()
print(f"Took {s1 - s0} ms")








