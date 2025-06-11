
class INA:
    def __init__(self, target):
        self.target = target
    def __private_Infinite_number_axis(self):
        target = abs(self.target)
        numMoves = 0
        sum_steps = 0
        while sum_steps < target or (sum_steps - target) % 2 != 0:
            numMoves += 1
            sum_steps += numMoves
        return numMoves
    def public_Infinite_number_axis(self):
        return self.__private_Infinite_number_axis()

#--------------:
print(INA(4).public_Infinite_number_axis() == 3)
print(INA(5).public_Infinite_number_axis() == 5)
print(INA(6).public_Infinite_number_axis() == 3)
