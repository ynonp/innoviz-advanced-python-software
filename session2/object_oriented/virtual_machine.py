class VirtualMachine:
    pass


if __name__ == '__main__':
    vm = VirtualMachine()
    vm.add(10)
    vm.add(20)
    vm.nop()

    print(vm.accumulator)

