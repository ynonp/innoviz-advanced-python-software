class Pet:
    def __init__(self, name):
        self.name = name
        self.age = 0

    def bark(self):
        print("Wuff, Wuff")

    def grow_up(self):
        self.age += 1

p = Pet("Rocky")
print(p.name)

q = Pet("Jimmy")
print(q.name)

p.bark()

p.grow_up()
p.grow_up()
p.grow_up()
print(p.age)


