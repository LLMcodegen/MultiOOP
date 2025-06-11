
class IBD:
    def __init__(self, rods):
        self.rods = rods
class SN_IBD(IBD):
    def Install_billboards(self):
        rods = self.rods
        dp = {0: 0}
        for rod in rods:
            cur_dp = dp.copy()
            for diff, y in cur_dp.items():
                dp[diff + rod] = max(dp.get(diff + rod, 0), y)
                new_diff = abs(diff - rod)
                dp[new_diff] = max(dp.get(new_diff, 0), y + min(diff, rod))
        return dp.get(0, 0)

#--------------:
print(SN_IBD([1, 1, 1, 1]).Install_billboards() == 2)
print(SN_IBD([2, 2, 2, 2]).Install_billboards() == 4)
print(SN_IBD([3, 3, 3, 3]).Install_billboards() == 6)
