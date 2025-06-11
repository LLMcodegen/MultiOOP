class FTMP:
    def Most_Points(self, points):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        n = len(points)
        if n < 2:
            return n
        max_points = 1
        for i in range(n):
            slopes = {}
            duplicates = 1
            verticals = 0
            cur_max = 0
            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                if dx == 0 and dy == 0:
                    duplicates += 1
                elif dx == 0:
                    verticals += 1
                else:
                    g = gcd(dx, dy)
                    slope = (dy // g, dx // g)
                    slopes[slope] = slopes.get(slope, 0) + 1
                    cur_max = max(cur_max, slopes[slope])
            max_points = max(max_points, cur_max + duplicates, verticals + duplicates)
        return max_points
#--------------:
print(FTMP().Most_Points([[0, 0], [0, 1], [0, 2], [0, 3], [1, 1], [1, 2]]) == 4)
print(FTMP().Most_Points([[1, 1], [1, 1], [2, 2], [3, 3]]) == 4)
print(FTMP().Most_Points([[2, 3], [4, 6], [6, 9], [8, 12], [10, 15]]) == 5)