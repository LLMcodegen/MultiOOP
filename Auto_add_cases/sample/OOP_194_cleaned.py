
class TC:
    def __init__(self, n):
        self.n = n
    def __private_There_continuity(self):
        def has_consecutive_ones(num):
            binary = bin(num)[2:]
            return '11' in binary
        count = 0
        for i in range(self.n + 1):
            if not has_consecutive_ones(i):
                count += 1
        return count
    def public_There_continuity(self):
        return self.__private_There_continuity()

#--------------:
print(TC(5).public_There_continuity() == 5) 
print(TC(6).public_There_continuity() == 5) 
print(TC(7).public_There_continuity() == 5) 
