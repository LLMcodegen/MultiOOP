
from collections import defaultdict
import math

class CCN:
    def __init__(self, nums):
        self.nums = nums
class SN_CCN(CCN):
    def Connected_components(self):
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        parent = list(range(len(self.nums)))
        factor_to_indices = defaultdict(list)
        for index, num in enumerate(self.nums):
            for factor in range(2, int(math.sqrt(num)) + 1):
                if num % factor == 0:
                    factor_to_indices[factor].append(index)
                    if factor != num // factor:
                        factor_to_indices[num // factor].append(index)
        for indices in factor_to_indices.values():
            for i in range(1, len(indices)):
                union(indices[0], indices[i])
        component_size = defaultdict(int)
        for i in range(len(self.nums)):
            root = find(i)
            component_size[root] += 1
        return max(component_size.values(), default=0)

#--------------:
print(SN_CCN([18, 27, 36, 45]).Connected_components() == 4)
print(SN_CCN([16, 24, 32, 40]).Connected_components() == 4)
print(SN_CCN([15, 25, 35, 45]).Connected_components() == 4)
