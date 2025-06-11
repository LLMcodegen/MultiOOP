
class RC:
    def __init__(self, trees):
        self.trees = trees
    def __private_Return_Coordinates(self):
        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - \
                   (a[1] - o[1]) * (b[0] - o[0])
        points = sorted(self.trees, key=lambda x: (x[0], x[1]))
        if len(points) <= 1:
            return points
        lower = []
        for p in points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
                lower.pop()
            lower.append(tuple(p))
        upper = []
        for p in reversed(points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) < 0:
                upper.pop()
            upper.append(tuple(p))
        full_hull = lower[:-1] + upper[:-1]
        unique_hull = list(set(full_hull))
        unique_hull_sorted = sorted(unique_hull, key=lambda x: (x[0], x[1]))
        return [list(point) for point in unique_hull_sorted]
    def public_Return_Coordinates(self):
        return self.__private_Return_Coordinates()

#--------------:
print(RC([[2, 2], [1, 3], [3, 3], [0, 0], [4, 4]]).public_Return_Coordinates() == [[0, 0], [1, 3], [2, 2], [3, 3], [4, 4]])
print(RC([[5, 5], [5, 6], [6, 5], [7, 7], [5, 7]]).public_Return_Coordinates() == [[5, 5], [5, 6], [5, 7], [6, 5], [7, 7]])
print(RC([[0, 0], [1, 1], [2, 0], [2, 2], [1, 2]]).public_Return_Coordinates() == [[0, 0], [1, 2], [2, 0], [2, 2]])
