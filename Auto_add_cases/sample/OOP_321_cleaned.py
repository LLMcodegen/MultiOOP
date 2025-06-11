
class NTS:
    def __init__(self, arr):
        self.arr = arr
class SN_NTS(NTS):
    def __init__(self, arr, target):
        super().__init__(arr)
        self.target = target
    def Number_tuples(self):
        count = 0
        n = len(self.arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if self.arr[i] + self.arr[j] + self.arr[k] == self.target:
                        count += 1
        return count

#--------------:
print(SN_NTS([1, 2, 3, 4, 5], 15).Number_tuples() == 0)
print(SN_NTS([1, 2, 3, 4, 5], 6).Number_tuples() == 1)
print(SN_NTS([1, 2, 3, 4, 5], 7).Number_tuples() == 1)
