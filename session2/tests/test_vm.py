import object_oriented.virtual_machine as virtual_machine

def test_accumulation():
    vm = virtual_machine.VirtualMachine()
    vm.add(10)
    vm.add(20)
    vm.nop()
    assert vm.accumulator == 30

