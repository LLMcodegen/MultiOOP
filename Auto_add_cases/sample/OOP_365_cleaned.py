
class TDN:
    def __init__(self, time):
        self.time = time
class SN_TDN(TDN):
    def Total_duration(self):
        count = 0
        remainder_count = [0] * 60
        for t in self.time:
            remainder = t % 60
            count += remainder_count[(60 - remainder) % 60]
            remainder_count[remainder] += 1
        return count

#--------------:
print(SN_TDN([30, 90, 150, 210]).Total_duration() == 6)
print(SN_TDN([10, 70, 130, 190]).Total_duration() == 0)
print(SN_TDN([5, 55, 115, 175]).Total_duration() == 3)
