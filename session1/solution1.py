from functools import reduce

def mymul(*numbers) -> float:
    result: float = 1
    for val in numbers:
        if type(val) == int or type(val) == float:
            result *= val

    return result


def mymul2(*numbers) -> float:
    return reduce(lambda acc, val: acc * val,
                  [n for n in numbers if type(n) == int],
                  1)


# returns 200:
print(mymul2('foo', 'bar', 10, 20))

# returns 1:
print(mymul2())

# returns 7:
print(mymul2(7))
