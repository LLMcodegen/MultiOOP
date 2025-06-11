
class PFG:
    def __init__(self, arr):
        self.arr = arr
class SN_PFG(PFG):
    def Pancake_flipping(self):
        def flip(sub_arr, k):
            sub_arr[:k] = sub_arr[:k][::-1]
            return sub_arr
        n = len(self.arr)
        res = []
        for i in range(n, 1, -1):
            max_index = self.arr.index(max(self.arr[:i]))
            if max_index != i - 1:
                if max_index != 0:
                    res.append(max_index + 1)
                    self.arr = flip(self.arr, max_index + 1)
                res.append(i)
                self.arr = flip(self.arr, i)
        return res

#--------------:
print(SN_PFG([6, 2, 7, 1, 4, 5, 3]).Pancake_flipping() == [3, 7, 5, 6, 3, 5, 2, 4, 3])
print(SN_PFG([9, 7, 6, 8, 5, 4, 3]).Pancake_flipping() == [7, 4, 6, 5, 3])
print(SN_PFG([5, 1, 2, 3, 4]).Pancake_flipping() == [5, 4])
