
class ESI:
    def __init__(self, matrix):
        self.matrix = matrix
class SN_ESI(ESI):
    def __init__(self, matrix, target):
        super().__init__(matrix)
        self.target = target
    def empty_submatrix(self):
        if not self.matrix or not self.matrix[0]:
            return 0
        rows, cols = len(self.matrix), len(self.matrix[0])
        count = 0
        for left in range(cols):
            sums = [0] * rows
            for right in range(left, cols):
                for row in range(rows):
                    sums[row] += self.matrix[row][right]
                count += self._count_target_sum(sums)
        return count
    def _count_target_sum(self, sums):
        count_map = {0: 1}
        current_sum, count = 0, 0
        for sum_val in sums:
            current_sum += sum_val
            count += count_map.get(current_sum - self.target, 0)
            count_map[current_sum] = count_map.get(current_sum, 0) + 1
        return count

#--------------:
print(SN_ESI([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0).empty_submatrix() == 0)
print(SN_ESI([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 0).empty_submatrix() == 11)
print(SN_ESI([[0, 1, 0], [1, 0, 1], [0, 1, 0]], 0).empty_submatrix() == 5)
