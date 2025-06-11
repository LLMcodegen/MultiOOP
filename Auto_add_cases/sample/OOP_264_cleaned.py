
from collections import deque, defaultdict

class TSN:
    def __init__(self, routes):
        self.routes = routes
class SN_TSN(TSN):
    def __init__(self, routes, source, target):
        super().__init__(routes)
        self.source = source
        self.target = target
    def Terminal_Station(self):
        if self.source == self.target:
            return 0
        stop_to_buses = defaultdict(list)
        for bus_idx, route in enumerate(self.routes):
            for stop in route:
                stop_to_buses[stop].append(bus_idx)
        queue = deque([(self.source, 0)])
        visited_stops = set([self.source])
        visited_buses = set()
        while queue:
            current_stop, buses_taken = queue.popleft()
            for bus in stop_to_buses[current_stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)
                for stop in self.routes[bus]:
                    if stop == self.target:
                        return buses_taken + 1
                    if stop not in visited_stops:
                        visited_stops.add(stop)
                        queue.append((stop, buses_taken + 1))
        return -1

#--------------:
print(SN_TSN([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 1, 5).Terminal_Station() == 2)
print(SN_TSN([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 1, 6).Terminal_Station() == 3)
print(SN_TSN([[1, 2, 3], [3, 4, 5], [5, 6, 7]], 1, 3).Terminal_Station() == 1)
