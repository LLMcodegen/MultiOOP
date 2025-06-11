
class RAI:
    def __init__(self, s, t):
        self.s = s
        self.t = t
    def __private_Random_addition(self):
        count_s = {}
        for char in self.s:
            count_s[char] = count_s.get(char, 0) + 1
        count_t = {}
        for char in self.t:
            count_t[char] = count_t.get(char, 0) + 1
        for char in count_t:
            if char not in count_s or count_t[char] != count_s[char]:
                return char
        return None
    def public_Random_addition(self):
        return self.__private_Random_addition()

#--------------:
print(RAI("python", "pythont").public_Random_addition() == "t")
print(RAI("world", "worldd").public_Random_addition() == "d")
print(RAI("game", "gamez").public_Random_addition() == "z")
