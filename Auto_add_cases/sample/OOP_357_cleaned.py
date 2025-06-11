
class SVE:
    def __init__(self, equations):
        self.equations = equations
class SN_SVE(SVE):
    def __init__(self, equations):
        super().__init__(equations)
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
    def union(self, parent, rank, x, y):
        rootX = self.find(parent, x)
        rootY = self.find(parent, y)
        if rootX != rootY:
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1
    def Single_variable(self):
        parent = {}
        rank = {}
        for eq in self.equations:
            a, op, b = eq[0], eq[1:3], eq[3]
            if a not in parent:
                parent[a] = a
                rank[a] = 0
            if b not in parent:
                parent[b] = b
                rank[b] = 0
            if op == "==":
                self.union(parent, rank, a, b)
        for eq in self.equations:
            a, op, b = eq[0], eq[1:3], eq[3]
            if op == "!=":
                if self.find(parent, a) == self.find(parent, b):
                    return False
        return True

#--------------:
print(SN_SVE(["a==b", "b==c", "c!=d", "d==a"]).Single_variable() == False)
print(SN_SVE(["a==b", "b==c", "c==d", "d!=a"]).Single_variable() == False)
print(SN_SVE(["a==b", "b!=c", "c==d", "d!=a"]).Single_variable() == True)
