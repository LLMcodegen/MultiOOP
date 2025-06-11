class CRTP:
    def climb_rooftop(self, n):
        if n <= 1:
            return 1
        first, second = 1, 1
        for i in range(2, n + 1):
            third = first + second
            first = second
            second = third
        return second
#--------------:
#--------------:
print(CRTP().climb_rooftop(6) == 13)
print(CRTP().climb_rooftop(7) == 21)
print(CRTP().climb_rooftop(8) == 34)
