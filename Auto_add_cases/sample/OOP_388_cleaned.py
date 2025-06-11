
class OEH:
    def __init__(self, arr):
        self.arr = arr
class SN_OEH(OEH):
    def One_exchange(self):
        arr = self.arr.copy()
        n = len(arr)
        max_i = -1
        max_j = -1
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i, -1):
                if arr[i] > arr[j]:
                    if max_i == -1 or i > max_i or (i == max_i and arr[j] > arr[max_j]):
                        max_i = i
                        max_j = j
        if max_i != -1:
            arr[max_i], arr[max_j] = arr[max_j], arr[max_i]
        return arr

#--------------:
print(SN_OEH([1, 3, 2]).One_exchange() == [1, 2, 3])
print(SN_OEH([1, 2, 3]).One_exchange() == [1, 2, 3])
print(SN_OEH([3, 1, 2]).One_exchange() == [2, 1, 3])
