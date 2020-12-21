# Generators
import itertools

# Create a generator that returns the sequence
# 1, 4, 9, 16, 25, ...
def squares():
    pass


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


def squares():
    # Generator Comprehension
    yield from (n * n for n in itertools.count(1))


def squares_easy():
    n = 1
    while True:
        yield n * n
        n += 1

for value in itertools.islice(squares(), 10):
    print(value)





