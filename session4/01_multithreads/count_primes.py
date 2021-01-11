from math import *
import threading, time

"""
Your Task:
Run count_primes in multiple threads (2 threads, 4 threads)
And check if it found the result faster and was still accurate

All files are in github:
http://github.com/ynonp/innoviz-advanced-python-software 
"""


class PrimesCounter(threading.Thread):
    def __init__(self, start, stop):
        super().__init__()
        self.__id = id
        self.__start = start
        self.__stop = stop
        self.result = 0

    def run(self):
        self.result = count_primes(self.__start, self.__stop)


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

print("Count Primes (single)")
s0 = time.time()
print(count_primes(1, 1_000_000))
s1 = time.time()
print(f"Took {s1 - s0} ms")

print("Count Primes (4)")
s0 = time.time()
w1 = PrimesCounter(1, 250_000)
w2 = PrimesCounter(250_000, 500_000)
w3 = PrimesCounter(500_000, 750_000)
w4 = PrimesCounter(750_000, 1_000_000)

for w in [w1, w2, w3, w4]:
    w.start()

for w in [w1, w2, w3, w4]:
    w.join()

print(sum([w.result for w in [w1, w2, w3, w4]]))
s1 = time.time()
print(f"Took {s1 - s0} ms")








