
class MOS:
    def __init__(self, startValue):
        self.startValue = startValue
class SN_MOS(MOS):
    def __init__(self, startValue, target):
        super().__init__(startValue)
        self.target = target
    def Minimum_operands(self):
        operations = 0
        current_value = self.startValue
        target = self.target
        while current_value != target:
            if target % 2 == 0 and target > current_value:
                target //= 2
            else:
                target += 1
            operations += 1
        return operations

#--------------:
print(SN_MOS(100, 1).Minimum_operands() == 99)
print(SN_MOS(1, 2).Minimum_operands() == 1)
print(SN_MOS(2, 1).Minimum_operands() == 1)
