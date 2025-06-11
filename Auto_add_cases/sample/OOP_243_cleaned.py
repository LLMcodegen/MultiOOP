
class MNB:
    def __init__(self, arr):
        self.arr = arr
    def __private_Maximum_number_blocks(self):
        arr = self.arr
        sorted_arr = sorted(arr)
        count = 0
        count_arr = {}
        count_sorted_arr = {}
        for i in range(len(arr)):
            a = arr[i]
            s = sorted_arr[i]
            count_arr[a] = count_arr.get(a, 0) + 1
            count_sorted_arr[s] = count_sorted_arr.get(s, 0) + 1
            if count_arr == count_sorted_arr:
                count += 1
        return count
    def public_Maximum_number_blocks(self):
        return self.__private_Maximum_number_blocks()

#--------------:
print(MNB([1, 2, 2, 1]).public_Maximum_number_blocks() == 2)
print(MNB([4, 2, 1, 3]).public_Maximum_number_blocks() == 1)
print(MNB([1, 5, 2, 4, 3]).public_Maximum_number_blocks() == 2)