
class SNS:
    def __init__(self, n):
        self.n = n
class SN_SNS(SNS):
    def __init__(self, n):
        super().__init__(n)
    def Sum_Numbers(self):
        n = self.n
        count = 0
        max_k = int((2 * n) ** 0.5) + 1
        for k in range(1, max_k):
            numerator = n - k * (k - 1) // 2
            if numerator <= 0:
                break
            if numerator % k == 0:
                m = numerator // k
                if m > 0:
                    count += 1
        return count

#--------------:
print(SN_SNS(6).Sum_Numbers() == 2)
print(SN_SNS(7).Sum_Numbers() == 2)
print(SN_SNS(8).Sum_Numbers() == 1)
