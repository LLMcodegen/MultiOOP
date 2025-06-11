
class CQ:
    def __init__(self, n):
        self.n = n
    def _private_Construction_quantity(self, n, used, pos):
        if pos > n:
            return 1
        count = 0
        for i in range(1, n + 1):
            if not used[i] and (i % pos == 0 or pos % i == 0):
                used[i] = True
                count += self._private_Construction_quantity(n, used, pos + 1)
                used[i] = False
        return count
    def public_Construction_quantity(self):
        used = [False] * (self.n + 1)
        return self._private_Construction_quantity(self.n, used, 1)

#--------------:
print(CQ(6).public_Construction_quantity() == 36)
print(CQ(7).public_Construction_quantity() == 41)