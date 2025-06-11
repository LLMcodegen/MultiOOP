
class MSI:
    def __init__(self, strs):
        self.strs = strs
class SN_MSI(MSI):
    def Minimum_spossible(self):
        strs = self.strs
        n = len(strs)
        if n == 0:
            return 0
        m = len(strs[0])
        dp = [1] * m
        for i in range(m):
            for j in range(i):
                is_valid = True
                for s in strs:
                    if s[j] > s[i]:
                        is_valid = False
                        break
                if is_valid:
                    dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(dp)
        return m - max_length

#--------------:
print(SN_MSI(["a", "b", "c"]).Minimum_spossible() == 0)
print(SN_MSI(["c", "b", "a"]).Minimum_spossible() == 0)
print(SN_MSI(["aaa", "bbb", "ccc"]).Minimum_spossible() == 0)
