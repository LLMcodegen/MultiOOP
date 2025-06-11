import functools

class SMG:
    def __init__(self, stones):
        self.stones = stones
class SN_SMG(SMG):
    def __init__(self, stones, K):
        super().__init__(stones)
        self.K = K
    def Stone_Merge(self):
        n = len(self.stones)
        if (n - 1) % (self.K - 1) != 0:
            return -1
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + self.stones[i]
        @functools.lru_cache(maxsize=None)
        def dp(i, j, m):
            if (j - i + 1 - m) % (self.K - 1) != 0:
                return float('inf')
            if i == j:
                return 0 if m == 1 else float('inf')
            if m == 1:
                return dp(i, j, self.K) + prefix[j + 1] - prefix[i]
            return min(dp(i, mid, 1) + dp(mid + 1, j, m - 1) for mid in range(i, j, self.K - 1))
        result = dp(0, n - 1, 1)
        return result if result != float('inf') else -1

#--------------:
print(SN_SMG([1, 1, 1, 1, 1], 2).Stone_Merge() == 12)
print(SN_SMG([1, 1, 1, 1, 1], 3).Stone_Merge() == 8)
print(SN_SMG([1, 1, 1, 1, 1], 4).Stone_Merge() == -1)
