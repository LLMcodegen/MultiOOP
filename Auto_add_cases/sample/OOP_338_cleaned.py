
class MPL:
    def __init__(self, strs):
        self.strs = strs
class SN_MPL(MPL):
    def Minimum_possible(self):
        strs = self.strs
        n = len(strs)
        if n == 0:
            return 0
        m = len(strs[0])
        ans = 0
        sorted_pairs = [False] * (n - 1)
        for i in range(m):
            delete_column = False
            for j in range(n - 1):
                if not sorted_pairs[j] and strs[j][i] > strs[j + 1][i]:
                    delete_column = True
                    break
            if delete_column:
                ans += 1
            else:
                for j in range(n - 1):
                    if strs[j][i] < strs[j + 1][i]:
                        sorted_pairs[j] = True
        return ans

#--------------:
print(SN_MPL(["a", "b", "c"]).Minimum_possible() == 0)
print(SN_MPL(["c", "b", "a"]).Minimum_possible() == 1)
print(SN_MPL(["aaa", "bbb", "ccc"]).Minimum_possible() == 0)
