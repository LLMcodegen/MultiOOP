
class RSC:
    def __init__(self, intervals):
        self.intervals = intervals
    def __private_Right_section(self):
        sorted_intervals = sorted(enumerate(self.intervals), key=lambda x: x[1][0])
        result = [-1] * len(self.intervals)
        for i, (start_i, end_i) in sorted_intervals:
            left, right = 0, len(sorted_intervals) - 1
            while left <= right:
                mid = (left + right) // 2
                start_mid, _ = sorted_intervals[mid][1]
                if start_mid >= end_i:
                    result[i] = sorted_intervals[mid][0]
                    right = mid - 1
                else:
                    left = mid + 1
        return result
    def public_Right_section(self):
        return self.__private_Right_section()

#--------------:
print(RSC([[1, 3], [3, 6], [6, 9], [9, 12]]).public_Right_section() == [1, 2, 3, -1])
print(RSC([[1, 2], [4, 5], [3, 6], [7, 8]]).public_Right_section() == [2, 3, 3, -1])
print(RSC([[1, 5], [2, 6], [4, 8], [5, 9]]).public_Right_section() == [3, -1, -1, -1])
