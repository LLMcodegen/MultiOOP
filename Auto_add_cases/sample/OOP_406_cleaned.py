
class MES:
    def __init__(self, arr1):
        self.arr1 = arr1
class SN_MES(MES):
    def __init__(self, arr1, arr2):
        super().__init__(arr1)
        self.arr2 = arr2
    def Maximum_expression(self):
        max_val = float('-inf')
        n = len(self.arr1)
        for i in range(n):
            for j in range(n):
                val = abs(self.arr1[i] - self.arr1[j]) + abs(self.arr2[i] - self.arr2[j]) + abs(i - j)
                max_val = max(max_val, val)
        return max_val

#--------------:
print(SN_MES([2, 2, 3], [3, 2, 1]).Maximum_expression() == 5)
print(SN_MES([3, 2, 3], [3, 2, 1]).Maximum_expression() == 4)
print(SN_MES([4, 2, 3], [3, 2, 1]).Maximum_expression() == 5)
