
class CLA:
    def __init__(self, n):
        self.n = n
    def __private_Complete_ladder(self):
        rows = 0
        while self.n >= rows + 1:
            rows += 1
            self.n -= rows
        return rows
    def public_Complete_ladder(self):
        return self.__private_Complete_ladder()

#--------------:
print(CLA(21).public_Complete_ladder() == 6)
print(CLA(28).public_Complete_ladder() == 7)
print(CLA(36).public_Complete_ladder() == 8)
