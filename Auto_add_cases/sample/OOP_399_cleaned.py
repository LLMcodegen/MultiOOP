
class PPG:
    def __init__(self, trips):
        self.trips = trips
class SN_PPG(PPG):
    def __init__(self, trips, capacity):
        super().__init__(trips)
        self.capacity = capacity
    def Pick_passengers(self):
        max_to = max(trip[2] for trip in self.trips)
        passengers = [0] * (max_to + 1)
        for num_passengers, from_km, to_km in self.trips:
            passengers[from_km] += num_passengers
            passengers[to_km] -= num_passengers
        current_passengers = 0
        for i in range(max_to + 1):
            current_passengers += passengers[i]
            if current_passengers > self.capacity:
                return False
        return True

#--------------:
print(SN_PPG([[2, 1, 5], [3, 5, 7]], 6).Pick_passengers() == True)
print(SN_PPG([[2, 1, 5], [3, 3, 7]], 3).Pick_passengers() == False)
print(SN_PPG([[2, 1, 5], [3, 5, 7]], 3).Pick_passengers() == True)
