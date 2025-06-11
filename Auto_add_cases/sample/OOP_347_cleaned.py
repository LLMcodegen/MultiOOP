
class SIG:
    def __init__(self, x):
        self.x = x
class SN_SIG(SIG):
    def __init__(self, x, y, bound):
        super().__init__(x)
        self.y = y
        self.bound = bound
    def Strong_integer(self):
        powerful_integers = set()
        i = 0
        while self.x ** i <= self.bound:
            j = 0
            while self.x ** i + self.y ** j <= self.bound:
                powerful_integers.add(self.x ** i + self.y ** j)
                if self.y == 1:
                    break
                j += 1
            if self.x == 1:
                break
            i += 1
        return list(powerful_integers)

#--------------:
print(SN_SIG(2, 3, 3).Strong_integer() == [2, 3])
print(SN_SIG(2, 3, 4).Strong_integer() == [2, 3, 4])
print(SN_SIG(2, 3, 5).Strong_integer() == [2, 3, 4, 5])
