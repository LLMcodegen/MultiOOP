
class IIG:
    def __init__(self, n):
        self.n = n
    def __private_Infinite_integers(self):
        length = 1
        count = 9
        start = 1
        while self.n > length * count:
            self.n -= length * count
            length += 1
            count *= 10
            start *= 10
        number = start + (self.n - 1) // length
        digit_index = (self.n - 1) % length
        return int(str(number)[digit_index])
    def public_Infinite_integers(self):
        return self.__private_Infinite_integers()

#--------------:
print(IIG(20).public_Infinite_integers() == 1)
print(IIG(21).public_Infinite_integers() == 5)
print(IIG(30).public_Infinite_integers() == 2)
