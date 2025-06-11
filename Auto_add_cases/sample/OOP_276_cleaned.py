
class ENS:
    def __init__(self, n):
        self.n = n
class SN_ENS(ENS):
    def __init__(self, n, k, maxPts):
        super().__init__(n)
        self.k = k
        self.maxPts = maxPts
    def Extract_Numbers(self):
        n, k, maxPts = self.n, self.k, self.maxPts
        if k == 0 or n >= k + maxPts:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0
        result = 0.0
        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            else:
                result += dp[i]
            if i - maxPts >= 0:
                if i - maxPts < k:
                    window_sum -= dp[i - maxPts]
        return round(result, 5)

#--------------:
print(SN_ENS(5, 2, 3).Extract_Numbers() == 1.0)
print(SN_ENS(10, 5, 2).Extract_Numbers() == 1.0)
print(SN_ENS(10, 5, 10).Extract_Numbers() == 0.87846)
