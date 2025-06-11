class HTRW:
    def __init__(self):
        pass
    def harvest_rainwater(self, heights):
        if not heights:
            return 0
        n = len(heights)
        left_max = [0] * n
        right_max = [0] * n
        water_collected = 0
        left_max[0] = heights[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], heights[i])
        right_max[n - 1] = heights[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], heights[i])
        for i in range(n):
            water_collected += min(left_max[i], right_max[i]) - heights[i]
        return water_collected
#--------------:
print(HTRW().harvest_rainwater([1, 0, 2, 1, 2, 1, 2]) == 3)
print(HTRW().harvest_rainwater([2, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 8)
print(HTRW().harvest_rainwater([4, 2, 0, 3, 2, 5]) == 9)
