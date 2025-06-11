class MOLI:
    def merge_overlapping_intervals(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged = []
        current_interval = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= current_interval[1]:
                current_interval[1] = max(current_interval[1], interval[1])
            else:
                merged.append(current_interval)
                current_interval = interval
        merged.append(current_interval)
        return merged
#--------------:
#--------------:
print(MOLI().merge_overlapping_intervals([[6, 8], [1, 9], [2, 4], [4, 7]]) == [[1, 9]])
print(MOLI().merge_overlapping_intervals([[1, 4], [2, 5], [5, 6]]) == [[1, 6]])
print(MOLI().merge_overlapping_intervals([[1, 2], [2, 3], [3, 4], [4, 5]]) == [[1, 5]])
