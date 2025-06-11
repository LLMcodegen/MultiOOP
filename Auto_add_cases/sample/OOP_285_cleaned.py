
class ASG:
    def __init__(self, seats):
        self.seats = seats
class SN_ASG(ASG):
    def Maximized_seating(self):
        max_distance = 0
        last_person = -1
        n = len(self.seats)
        for i in range(n):
            if self.seats[i] == 1:
                if last_person == -1:
                    max_distance = i
                else:
                    max_distance = max(max_distance, (i - last_person) // 2)
                last_person = i
        if self.seats[-1] == 0:
            max_distance = max(max_distance, n - 1 - last_person)
        return max_distance

#--------------:
print(SN_ASG([0, 0, 1, 0, 0]).Maximized_seating() == 2)
print(SN_ASG([1, 0, 0, 0, 1]).Maximized_seating() == 2)
print(SN_ASG([0, 0, 0, 0, 1]).Maximized_seating() == 4)
