
class MNS:
    def __init__(self, n):
        self.n = n
class SN_MNS(MNS):
    def __init__(self, n, a, b):
        super().__init__(n)
        self.a = a
        self.b = b
    def gcd(self, x, y):
        while y:
            x, y = y, x % y
        return x
    def lcm(self, x, y):
        return x * y // self.gcd(x, y)
    def Magical_Numbers(self):
        lcm_ab = self.lcm(self.a, self.b)
        left, right = 1, self.n * min(self.a, self.b)
        while left < right:
            mid = (left + right) // 2
            if mid // self.a + mid // self.b - mid // lcm_ab < self.n:
                left = mid + 1
            else:
                right = mid
        return left

#--------------:
print(SN_MNS(6, 2, 3).Magical_Numbers() == 9)
print(SN_MNS(7, 2, 3).Magical_Numbers() == 10)
print(SN_MNS(8, 2, 3).Magical_Numbers() == 12)
