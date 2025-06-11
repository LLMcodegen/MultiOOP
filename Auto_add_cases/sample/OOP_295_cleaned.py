
class PAY:
    def __init__(self, arr):
        self.arr = arr
class SN_PAY(PAY):
    def Positive_array(self):
        n = len(self.arr)
        if n < 3:
            return 0
        num_set = set(self.arr)
        longest_length = 0
        dp = {}
        for k in range(n):
            for j in range(k):
                i = self.arr[k] - self.arr[j]
                if i in num_set and i < self.arr[j]:
                    dp[j, k] = dp.get((i, j), 2) + 1
                    longest_length = max(longest_length, dp[j, k])
        return longest_length if longest_length >= 3 else 0

#--------------:
print(SN_PAY([1, 2, 3, 5, 8, 13]).Positive_array() == 3)
print(SN_PAY([1, 2, 3, 5, 8, 13, 21]).Positive_array() == 3)
print(SN_PAY([1, 2, 3, 5, 8, 13, 21, 34]).Positive_array() == 3)
