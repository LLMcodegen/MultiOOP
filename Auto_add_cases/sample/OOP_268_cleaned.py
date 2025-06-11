
class RIR:
    def __init__(self, arr):
        self.arr = arr
class SN_RIR(RIR):
    def repeating_integer(self):
        arr = sorted(self.arr)
        MOD = 10**9 + 7
        dp = {x: 1 for x in arr}
        index_map = {x: i for i, x in enumerate(arr)}
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    factor = arr[i] // arr[j]
                    if factor in index_map:
                        dp[arr[i]] += dp[arr[j]] * dp[factor]
                        dp[arr[i]] %= MOD
        return sum(dp.values()) % MOD

#--------------:
print(SN_RIR([1, 2, 3, 4, 6, 12, 24, 36]).repeating_integer() == 839)
print(SN_RIR([1, 2, 3, 4, 6, 12, 24, 36, 48]).repeating_integer() == 3177)
print(SN_RIR([1, 2, 3, 4, 6, 12, 24, 36, 48, 60]).repeating_integer() == 3179)
