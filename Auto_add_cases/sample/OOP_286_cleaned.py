
class TAR:
    def __init__(self, rectangles):
        self.rectangles = rectangles
class SN_TAR(TAR):
    def total_area(self):
        MOD = 10**9 + 7
        events = []
        for x1, y1, x2, y2 in self.rectangles:
            events.append((x1, 1, y1, y2))
            events.append((x2, -1, y1, y2))
        events.sort()
        active = []
        prev_x = events[0][0]
        area = 0
        def calc_y_union():
            total = 0
            prev_y = -1
            for y1, y2 in active:
                prev_y = max(prev_y, y1)
                total += max(0, y2 - prev_y)
                prev_y = max(prev_y, y2)
            return total
        for x, typ, y1, y2 in events:
            area += calc_y_union() * (x - prev_x)
            area %= MOD
            if typ == 1:
                active.append((y1, y2))
                active.sort()
            else:
                active.remove((y1, y2))
            prev_x = x
        return area

#--------------:
print(SN_TAR([[0, 0, 2, 2]]).total_area() == 4)
print(SN_TAR([[0, 0, 2, 2], [2, 0, 4, 2]]).total_area() == 8)
print(SN_TAR([[0, 0, 2, 2], [0, 2, 2, 4]]).total_area() == 8)
