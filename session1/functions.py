def add_stuff(x: float, y: float) -> float:
    return x + y


def rect(x, y, width, height, color):
    pass

def circle(x: int, y: int, *, color: str):
    pass

circle(10, 20, color='red')

# This won't work
circle(10, 20, 'red')



# Calling functions:

# Positional arguments
add_stuff(10, 20)

# Keyword arguments
# Both are the same
add_stuff(x=10, y=20)
add_stuff(y=20, x=10)

rect(40, 40, 100, 20, 'red')
rect(x=40, y=40, width=50, height=20, color='red')




