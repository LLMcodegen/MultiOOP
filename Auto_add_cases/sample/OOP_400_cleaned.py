
class MAR:
    def __init__(self, array):
        if len(array) < 3:
            raise ValueError("Array must have at least three elements.")
        self.array = array
class SN_MAR(MAR):
    def __init__(self, array, target):
        super().__init__(array)
        self.target = target
    def Mountain_array(self):
        peak_index = self.find_peak()
        index = self.binary_search(0, peak_index, True)
        if index != -1:
            return index
        return self.binary_search(peak_index + 1, len(self.array) - 1, False)
    def find_peak(self):
        left, right = 0, len(self.array) - 1
        while left < right:
            mid = (left + right) // 2
            if self.array[mid] < self.array[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
    def binary_search(self, left, right, is_ascending):
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == self.target:
                if is_ascending:
                    while mid > 0 and self.array[mid - 1] == self.target:
                        mid -= 1
                return mid
            if (self.array[mid] < self.target) == is_ascending:
                left = mid + 1
            else:
                right = mid - 1
        return -1

#--------------:
print(SN_MAR([1, 2, 3, 4, 5, 4, 3, 2, 1], 2).Mountain_array() == 1)
print(SN_MAR([1, 2, 3, 4, 5, 4, 3, 2, 1], 3).Mountain_array() == 2)
print(SN_MAR([1, 2, 3, 4, 5, 4, 3, 2, 1], 6).Mountain_array() == -1)
