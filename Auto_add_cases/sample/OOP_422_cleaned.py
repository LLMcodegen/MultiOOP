
class MBG:
    def __init__(self, s):
        self.s = s
class SN_MBG(MBG):
    def __init__(self, s, t, maxCost):
        super().__init__(s)
        self.t = t
        self.maxCost = maxCost
    def Maximum_budget(self):
        if len(self.s) != len(self.t):
            raise ValueError("Strings s and t must be of equal length")
        n = len(self.s)
        max_length = 0
        current_cost = 0
        left = 0
        for right in range(n):
            current_cost += abs(ord(self.s[right]) - ord(self.t[right]))
            while current_cost > self.maxCost:
                current_cost -= abs(ord(self.s[left]) - ord(self.t[left]))
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

#--------------:
print(SN_MBG("aacd", "acde", 3).Maximum_budget() == 3)
print(SN_MBG("ascd", "acde", 4).Maximum_budget() == 2)
print(SN_MBG("adcd", "acde", 5).Maximum_budget() == 4)
