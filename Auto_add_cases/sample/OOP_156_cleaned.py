
class IZOE:
    def __init__(self, s: str):
        self.s = s
    def __private_Infinity_Zone(self) -> int:
        base = "abcdefghijklmnopqrstuvwxyz" * 2
        substrings = set()
        for i in range(len(self.s)):
            for j in range(i + 1, len(self.s) + 1):
                substring = self.s[i:j]
                if substring in base:
                    substrings.add(substring)
        return len(substrings)
    def public_Infinity_Zone(self) -> int:
        return self.__private_Infinity_Zone()

#--------------:
print(IZOE("xyz").public_Infinity_Zone() == 6)
print(IZOE("aaa").public_Infinity_Zone() == 1)
print(IZOE("abcde").public_Infinity_Zone() == 15)
