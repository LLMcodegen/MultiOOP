
class ES:
    def __init__(self, row):
        self.row = row
    def __private_Exchange_seats(self):
        n = len(self.row) // 2
        positions = {person: i for i, person in enumerate(self.row)}
        swaps = 0
        for i in range(n):
            person1 = self.row[2 * i]
            person2 = self.row[2 * i + 1]
            if person1 // 2 != person2 // 2:
                partner_of_person1 = person1 + 1 if person1 % 2 == 0 else person1 - 1
                partner_seat = positions[partner_of_person1]
                self.row[2 * i + 1], self.row[partner_seat] = self.row[partner_seat], self.row[2 * i + 1]
                positions[person2] = partner_seat
                positions[partner_of_person1] = 2 * i + 1
                swaps += 1
        return swaps
    def public_Exchange_seats(self):
        return self.__private_Exchange_seats()

#--------------:
print(ES([0, 2, 3, 1]).public_Exchange_seats() == 1)
print(ES([0, 3, 2, 1]).public_Exchange_seats() == 1)
print(ES([1, 0, 3, 2]).public_Exchange_seats() == 0)
