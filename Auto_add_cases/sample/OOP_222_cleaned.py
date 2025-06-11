
class BS:
    def __init__(self, positions):
        self.positions = positions
    def _private_Block_stacking(self):
        skyline = []
        max_heights = []
        for block in self.positions:
            left, side_length = block
            right = left + side_length
            current_height = 0
            for i in range(left, right):
                if i < len(skyline):
                    current_height = max(current_height, skyline[i])
                else:
                    skyline.extend([0] * (i - len(skyline) + 1))
                    current_height = max(current_height, skyline[i])
            for i in range(left, right):
                skyline[i] = current_height + side_length
            max_heights.append(max(skyline))
        return max_heights
    def public_Block_stacking(self):
        return self._private_Block_stacking()

#--------------:
print(BS([[1, 2], [3, 2], [5, 2], [7, 2], [9, 2], [11, 2]]).public_Block_stacking() == [2, 2, 2, 2, 2, 2])
print(BS([[1, 2], [3, 2], [5, 2], [7, 2], [9, 2], [11, 2], [13, 2]]).public_Block_stacking() == [2, 2, 2, 2, 2, 2, 2])
print(BS([[1, 2], [3, 2], [5, 2], [7, 2], [9, 2], [11, 2], [13, 2], [15, 2]]).public_Block_stacking() == [2, 2, 2, 2, 2, 2, 2, 2])
