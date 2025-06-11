
class PCN:
    def __init__(self, rectangles):
        self.rectangles = rectangles
    def __private_Parallel_coordinate(self):
        total_area = 0
        min_x = min_y = float('inf')
        max_a = max_b = float('-inf')
        corners = set()
        for x, y, a, b in self.rectangles:
            total_area += (a - x) * (b - y)
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            for corner in [(x, y), (x, b), (a, y), (a, b)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)
        if len(corners) != 4 or (min_x, min_y) not in corners or (min_x, max_b) not in corners or (max_a, min_y) not in corners or (max_a, max_b) not in corners:
            return False
        bounding_area = (max_a - min_x) * (max_b - min_y)
        return total_area == bounding_area
    def public_Parallel_coordinate(self):
        return self.__private_Parallel_coordinate()

#--------------:
print(PCN([[0, 0, 2, 2], [2, 0, 4, 2], [0, 2, 2, 4], [2, 2, 4, 4]]).public_Parallel_coordinate() == True)
print(PCN([[1, 1, 3, 3], [3, 1, 4, 3], [1, 3, 4, 4]]).public_Parallel_coordinate() == True)
print(PCN([[1, 1, 3, 3], [1, 3, 2, 4]]).public_Parallel_coordinate() == False)
