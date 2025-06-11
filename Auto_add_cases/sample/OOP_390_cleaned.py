from collections import defaultdict

class EST:
    def __init__(self, s1):
        self.s1 = s1
class SN_EST(EST):
    def __init__(self, s1, s2, baseStr):
        super().__init__(s1)
        self.s2 = s2
        self.baseStr = baseStr
    def find_equivalence(self):
        equivalence = defaultdict(set)
        for a, b in zip(self.s1, self.s2):
            equivalence[a].add(b)
            equivalence[b].add(a)
        parent = {}
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX
        for a, b in zip(self.s1, self.s2):
            if a not in parent:
                parent[a] = a
            if b not in parent:
                parent[b] = b
            union(a, b)
        groups = defaultdict(list)
        for char in parent.keys():
            root = find(char)
            groups[root].append(char)
        min_mapping = {}
        for group in groups.values():
            smallest = min(group)
            for char in group:
                min_mapping[char] = smallest
        result = []
        for char in self.baseStr:
            if char in min_mapping:
                result.append(min_mapping[char])
            else:
                result.append(char)
        return ''.join(result)
    def Equivalent_String(self):
        return self.find_equivalence()

#--------------:
print(SN_EST("abcd", "efgh", "dcba").Equivalent_String() == "dcba")
print(SN_EST("pqrs", "stuv", "srqp").Equivalent_String() == "prqp")
print(SN_EST("wxyz", "zyxw", "yxwz").Equivalent_String() == "xxww")
