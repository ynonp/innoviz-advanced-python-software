# Generators
import itertools

def fib():
    a, b = 0, 1
    while True:
        print(f"Calculating... a = {a}")
        a, b = b, a + b
        yield a

#def slice(g, size):
#    for i in range(size):
#        yield next(g)



# What's the sum of the first 10 fibonacci numbers?
#res = sum([fib(i) for i in range(10)])

res = 0
for value in itertools.islice(fib(), 10):
    res += value # next - forward till the next "yield"

print(res)
