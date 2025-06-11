
class RSA:
    def __init__(self, bookings):
        self.bookings = bookings
class SN_RSA(RSA):
    def __init__(self, bookings, n):
        super().__init__(bookings)
        self.n = n
    def Reserved_seats(self):
        answer = [0] * self.n
        for first, last, seats in self.bookings:
            answer[first - 1] += seats
            if last < self.n:
                answer[last] -= seats
        for i in range(1, self.n):
            answer[i] += answer[i - 1]
        return answer

#--------------:
print(SN_RSA([[1, 2, 10]], 5).Reserved_seats() == [10, 10, 0, 0, 0])
print(SN_RSA([[1, 2, 10], [2, 3, 5], [3, 5, 2]], 5).Reserved_seats() == [10, 15, 7, 2, 2])
print(SN_RSA([[1, 5, 3]], 5).Reserved_seats() == [3, 3, 3, 3, 3])