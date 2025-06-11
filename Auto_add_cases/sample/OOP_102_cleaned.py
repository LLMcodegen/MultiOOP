
class CVA:
    def __init__(self, distance):
        self.distance = distance
    def _private_Counterclockwise_variation(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        path = [(x, y)]
        direction = 0
        for dist in self.distance:
            for _ in range(dist):
                x += directions[direction][0]
                y += directions[direction][1]
                if (x, y) in path:
                    return True
                path.append((x, y))
            direction = (direction + 1) % 4
        return False
    def public_Counterclockwise_variation(self):
        return self._private_Counterclockwise_variation()

#--------------:
print(CVA([1, 1, 2, 1, 1]).public_Counterclockwise_variation() == True)
print(CVA([3, 2, 3, 1, 2]).public_Counterclockwise_variation() == False)