class VirtualMachine:
    def __init__(self):
        self.accumulator = 0
        self.commands = []
        self.ip = 0

    def add(self, n):
        self.commands.append(Command("add", n))

    def skip(self, n):
        self.commands.append(Command("skip", n))

    def nop(self):
        self.commands.append(Command("nop"))

    def run(self):
        while self.ip < len(self.commands):
            cmd = self.commands[self.ip]
            cmd.run(self)
            self.ip += 1


def Command(command_name, *params):
    if command_name == 'add':
        return CommandAdd(params[0])
    elif command_name == 'skip':
        return CommandSkip(params[0])
    elif command_name == 'nop':
        return CommandNop()


class CommandAdd:
    def __init__(self, n):
        self.n = n

    def run(self, vm):
        vm.accumulator += self.n


class CommandSkip:
    def __init__(self, n):
        self.n = n

    def run(self, vm):
        vm.ip += self.n


class CommandNop:
    def run(self, vm):
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



