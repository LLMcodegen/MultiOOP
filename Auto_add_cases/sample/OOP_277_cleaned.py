
class SST:
    def __init__(self, strs):
        self.strs = strs
class SN_SST(SST):
    def Similar_Strings(self):
        def are_similar(s1, s2):
            diff = sum(1 for a, b in zip(s1, s2) if a != b)
            return diff == 2 or diff == 0
        def find_groups():
            visited = set()
            groups = 0  
            for i in range(len(self.strs)):
                if i not in visited:
                    groups += 1
                    stack = [i]
                    while stack:
                        current = stack.pop()
                        visited.add(current)
                        for j in range(len(self.strs)):
                            if j not in visited and are_similar(self.strs[current], self.strs[j]):
                                stack.append(j)
            return groups
        return find_groups()

#--------------:
print(SN_SST(["abc", "abd", "acd"]).Similar_Strings() == 2)
print(SN_SST(["abc", "acb", "bac", "bca", "cab", "cba"]).Similar_Strings() == 1)
print(SN_SST(["abc", "def", "ghi"]).Similar_Strings() == 3)
