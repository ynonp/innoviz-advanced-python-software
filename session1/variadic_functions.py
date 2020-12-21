from typing import List

def add_stuff(*xyz: int) -> int:
    return sum(xyz)


print(add_stuff(10, 20, 30))

data = [10, 20, 30]
print(add_stuff(*data))


