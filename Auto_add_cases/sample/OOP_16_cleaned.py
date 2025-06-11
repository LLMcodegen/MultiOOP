class FTGV:
    def find_target_value(self, sorted_array, target_value):
        left, right = 0, len(sorted_array) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_array[mid] == target_value:
                return mid
            elif sorted_array[mid] < target_value:
                left = mid + 1
            else:
                right = mid - 1
        return left
#--------------:
#--------------:
print(FTGV().find_target_value([1, 3, 5, 7, 9], 7) == 3)
print(FTGV().find_target_value([1, 3, 5, 7, 9], 8) == 4)
print(FTGV().find_target_value([100, 200, 300], 150) == 1)
