import object_oriented.virtual_machine as virtual_machine

def test_accumulation():
    vm = virtual_machine.VirtualMachine()
    vm.add(10)
    vm.add(20)
    vm.nop()
    vm.run()
    assert vm.accumulator == 30


def test_with_jumps():
    vm = virtual_machine.VirtualMachine()
    vm.add(10)
    vm.add(20)
    vm.jmp(2)
    vm.add(30)
    vm.add(40)
    vm.nop()

    vm.run()
    # Prints: 70
    assert vm.accumulator == 70
