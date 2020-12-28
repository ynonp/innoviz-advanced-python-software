class VirtualMachine:
    def __init__(self):
        self.accumulator = 0
        self.commands = []
        self.ip = 0

    def add(self, n):
        self.accumulator += n
        self.commands.append(Command("add", n))

    def skip(self, n):
        self.commands.append(Command("skip", n))

    def nop(self):
        self.commands.append(Command("nop"))

    def run(self):
        while self.ip < len(self.commands):
            cmd = self.commands[self.ip]
            # ???
            self.ip += 1

class Command:
    pass


if __name__ == '__main__':
    vm = VirtualMachine()
    vm.add(10)
    vm.add(20)
    vm.skip(1)
    vm.add(30)
    vm.add(40)
    vm.nop()

    vm.run()
    # Prints: 70
    print(vm.accumulator)



