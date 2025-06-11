class GTNOTZ:
    def get_trailing(self, n):
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count
#--------------:
print(GTNOTZ().get_trailing(100) == 24)
print(GTNOTZ().get_trailing(200) == 49)
print(GTNOTZ().get_trailing(30) == 7)
