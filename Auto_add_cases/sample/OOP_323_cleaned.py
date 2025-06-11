
class BVE:
    def __init__(self, arr):
        self.arr = arr
class SN_BVE(BVE):
    def Binary_values(self):
        arr = self.arr
        n = len(arr)
        total_ones = sum(arr)
        if total_ones == 0:
            return [0, n - 1] if n >= 3 else [-1, -1]
        if total_ones % 3 != 0:
            return [-1, -1]
        ones_per_part = total_ones // 3
        ones_indices = [i for i, bit in enumerate(arr) if bit == 1]
        i1, j1 = ones_indices[0], ones_indices[ones_per_part - 1]
        i2, j2 = ones_indices[ones_per_part], ones_indices[2 * ones_per_part - 1]
        i3, j3 = ones_indices[2 * ones_per_part], ones_indices[-1]
        part1 = arr[i1:j1 + 1]
        part2 = arr[i2:j2 + 1]
        part3 = arr[i3:j3 + 1]
        if part1 != part2 or part1 != part3:
            return [-1, -1]
        zeros_after_part1 = i2 - j1 - 1
        zeros_after_part2 = i3 - j2 - 1
        zeros_at_end = n - j3 - 1
        if zeros_after_part1 < zeros_at_end or zeros_after_part2 < zeros_at_end:
            return [-1, -1]
        i = j1 + zeros_at_end
        j = j2 + zeros_at_end + 1
        if i + 1 < j:
            return [i, j]
        else:
            return [-1, -1]

#--------------:
print(SN_BVE([1, 0, 0, 1, 0, 0, 1, 0, 0]).Binary_values() == [2, 6])
print(SN_BVE([1, 1, 1, 1, 1, 1, 1, 1, 1]).Binary_values() == [2, 6])
print(SN_BVE([0, 0, 0, 0, 0, 0, 0, 0, 0]).Binary_values() == [0, 8])
