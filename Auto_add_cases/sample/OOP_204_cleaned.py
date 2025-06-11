
class MNO:
    def __init__(self, n):
        self.n = n
    def __Minimum_operations(self):
        if self.n <= 1:
            return 0
        operations = 0
        divisor = 2
        remaining = self.n
        while remaining > 1:
            while remaining % divisor == 0:
                operations += divisor
                remaining //= divisor
            divisor += 1
        return operations
    def public_Minimum_operations(self):
        return self.__Minimum_operations()

#--------------:
print(MNO(27).public_Minimum_operations() == 9)
print(MNO(30).public_Minimum_operations() == 10)
print(MNO(50).public_Minimum_operations() == 12)
