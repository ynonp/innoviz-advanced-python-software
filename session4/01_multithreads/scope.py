# GLOBAL variable x
x = 10

def foo():
    global x
    print(x)

    if False:
        x = 10

foo()
