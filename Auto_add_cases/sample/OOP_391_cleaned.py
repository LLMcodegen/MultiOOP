
from collections import Counter

class MRW:
    def __init__(self, matrix):
        self.matrix = matrix
class SN_MRW(MRW):
    def Maximum_rows(self):
        row_patterns = [tuple(row) for row in self.matrix]
        pattern_counts = Counter(row_patterns)
        max_rows = 0
        seen = set()
        for pattern, count in pattern_counts.items():
            if pattern in seen:
                continue
            complement = tuple(1 - bit for bit in pattern)
            complement_count = pattern_counts.get(complement, 0)
            total = count + complement_count
            max_rows = max(max_rows, total)
            seen.add(pattern)
            seen.add(complement)
        return max_rows

#--------------:
print(SN_MRW([[1,1],[1,1],[0,0]]).Maximum_rows() == 3)
print(SN_MRW([[0,1],[0,0],[1,1]]).Maximum_rows() == 2)
print(SN_MRW([[1,0,0],[1,1,1],[0,1,1]]).Maximum_rows() == 2)
