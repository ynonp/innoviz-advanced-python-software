f = lambda x: x * 10

g = lambda x, y: max(x, y)
t = lambda x, y, z: [(i, j, k)  for i in range(x)
                                for j in range(y)
                                for k in range(z)
                                if i + j == k
                     ]

def hello():
    print("Hello world")

print(f(50))

print(t(10, 10, 10))


print(sorted(['one', 'two', 'three', 'four', 'five'],
             key=lambda item: item[-1]))
