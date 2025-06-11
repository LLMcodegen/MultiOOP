
class ESQ:
    def __init__(self, arr):
        self.arr = arr
class SN_ESQ(ESQ):
    def __init__(self, arr, difference):
        super().__init__(arr)
        self.difference = difference
    def Equidistant_subsequence(self):
        if not self.arr:
            return 0
        dp = {}
        max_length = 1
        for num in self.arr:
            if num - self.difference in dp:
                dp[num] = dp[num - self.difference] + 1
            else:
                dp[num] = 1
            max_length = max(max_length, dp[num])
        return max_length

#--------------:
print(SN_ESQ([1, 3, 5, 7, 9], 5).Equidistant_subsequence() == 1)
print(SN_ESQ([1, 3, 5, 7, 9], 6).Equidistant_subsequence() == 2)
print(SN_ESQ([1, 3, 5, 7, 9], 7).Equidistant_subsequence() == 1)
