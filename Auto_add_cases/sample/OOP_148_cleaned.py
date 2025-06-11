
from collections import Counter

class DODE:
    def __init__(self, s):
        self.s = s
    def __private_descending_order(self):
        char_freq = Counter(self.s)
        sorted_chars = sorted(char_freq, key=lambda x: (-char_freq[x], x))
        result = ''.join(char * char_freq[char] for char in sorted_chars)
        return result
    def public_descending_order(self):
        return self.__private_descending_order()

#--------------:
print(DODE("google").public_descending_order() == "ggooel")
print(DODE("aaaaaaa").public_descending_order() == "aaaaaaa")
print(DODE("zzyyxx").public_descending_order() == "xxyyzz")
