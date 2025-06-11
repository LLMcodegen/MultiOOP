
class NAS:
    def __init__(self, grid):
        self.grid = grid
class SN_NAS(NAS):
    def Number_areas(self):
        n = len(self.grid)
        parent = {}
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent[find(x)] = find(y)
        for i in range(n):
            for j in range(n):
                c = self.grid[i][j]
                root_indices = [(i, j, k) for k in range(4)]
                if c == ' ':
                    union(root_indices[0], root_indices[1])
                    union(root_indices[1], root_indices[2])
                    union(root_indices[2], root_indices[3])
                elif c == '/':
                    union(root_indices[0], root_indices[3])
                    union(root_indices[1], root_indices[2])
                elif c == '\\':
                    union(root_indices[0], root_indices[1])
                    union(root_indices[2], root_indices[3])
                if i + 1 < n:
                    union((i, j, 2), (i + 1, j, 0))
                if j + 1 < n:
                    union((i, j, 1), (i, j + 1, 3))
        regions = set()
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    regions.add(find((i, j, k)))
        return len(regions)

#--------------:
print(SN_NAS([" /", "\\ "]).Number_areas() == 2)
print(SN_NAS([" /", " /"]).Number_areas() == 2)
print(SN_NAS(["\\ ", "\\ "]).Number_areas() == 2)
