
class SII:
    def __init__(self, arr1):
        self.arr1 = arr1
class SN_SII(SII):
    def __init__(self, arr1, arr2):
        super().__init__(arr1)
        self.arr2 = sorted(set(arr2))
    def Strictly_Increasing(self):
        from bisect import bisect_right
        from functools import lru_cache
        arr1, arr2 = self.arr1, self.arr2
        n = len(arr1)
        @lru_cache(None)
        def dfs(i, prev):
            if i == n:
                return 0
            min_ops = float('inf')
            if arr1[i] > prev:
                min_ops = dfs(i + 1, arr1[i])
            idx = bisect_right(arr2, prev)
            if idx < len(arr2):
                ops = dfs(i + 1, arr2[idx]) + 1
                min_ops = min(min_ops, ops)
            return min_ops
        res = dfs(0, -float('inf'))
        return res if res != float('inf') else -1

#--------------:
print(SN_SII([1, 5, 3, 6, 7], [1, 6, 3, 6]).Strictly_Increasing() == -1)
print(SN_SII([1, 5, 3, 6, 7], [1, 6, 3, 7]).Strictly_Increasing() == -1)
print(SN_SII([1, 5, 3, 6, 7], [1, 6, 3, 8]).Strictly_Increasing() == -1)
