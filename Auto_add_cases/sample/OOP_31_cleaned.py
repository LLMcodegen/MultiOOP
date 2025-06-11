class STANOL:
    def sorted_non_overlapping(self, intervals, new_interval):
        merged = []
        i = 0
        while i < len(intervals) and intervals[i][1] < new_interval[0]:
            merged.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1
        merged.append(new_interval)
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        return merged
#--------------:
#--------------:
print(STANOL().sorted_non_overlapping([[1, 5]], [2, 3]) == [[1, 5]])
print(STANOL().sorted_non_overlapping([[1, 2], [3, 4], [5, 6]], [4, 5]) == [[1, 2], [3, 6]])
print(STANOL().sorted_non_overlapping([[1, 3], [6, 9]], [4, 5]) == [[1, 3], [4, 5], [6, 9]])
