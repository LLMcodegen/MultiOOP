
class MWG:
    def __init__(self, stones):
        self.stones = stones
class SN_MWG(MWG):
    def Minimum_weight(self):
        stones = self.stones
        total = sum(stones)
        max_weight = total // 2
        dp = [False] * (max_weight + 1)
        dp[0] = True
        for weight in stones:
            for i in range(max_weight, weight - 1, -1):
                if dp[i - weight]:
                    dp[i] = True
        for i in range(max_weight, -1, -1):
            if dp[i]:
                return total - 2 * i
        return 0

#--------------:
print(SN_MWG([7, 8, 9]).Minimum_weight() == 6)
print(SN_MWG([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).Minimum_weight() == 1)
print(SN_MWG([9, 10, 11]).Minimum_weight() == 8)
