
class STF:
    def __init__(self, arr):
        self.arr = arr
class SN_STF(STF):
    def __init__(self, arr, k):
        super().__init__(arr)
        self.k = k
    def Separation_transformation(self):
        n = len(self.arr)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            max_num = 0
            dp[i] = 0
            for l in range(1, min(i, self.k) + 1):
                max_num = max(max_num, self.arr[i - l])
                dp[i] = max(dp[i], dp[i - l] + max_num * l)
        return dp[n]

#--------------:
print(SN_STF([1, 2, 3, 4, 5], 3).Separation_transformation() == 19)
print(SN_STF([5, 4, 3, 2, 1], 3).Separation_transformation() == 19)
print(SN_STF([1, 2, 3, 4, 5], 4).Separation_transformation() == 21)
