
class UNB:
    def __init__(self, n):
        self.n = n
class SN_UNB(UNB):
    def __init__(self, n, a, b, c):
        super().__init__(n)
        self.a = a
        self.b = b
        self.c = c
    def count_ugly(self, x):
        return (x // self.a) + (x // self.b) + (x // self.c) \
               - (x // (self.a * self.b)) \
               - (x // (self.a * self.c)) \
               - (x // (self.b * self.c)) \
               + (x // (self.a * self.b * self.c))

    def Ugly_number(self):
        left, right = 1, 2 * 10**9
        while left < right:
            mid = (left + right) // 2
            if self.count_ugly(mid) < self.n:
                left = mid + 1
            else:
                right = mid
        return left

#--------------:
print(SN_UNB(2, 2, 3, 5).Ugly_number() == 3)
print(SN_UNB(6, 2, 3, 5).Ugly_number() == 8)
print(SN_UNB(7, 2, 3, 5).Ugly_number() == 9)
