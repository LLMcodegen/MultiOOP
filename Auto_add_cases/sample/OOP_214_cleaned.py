
class OS:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __private_Overlay_substring(self):
        if self.b in self.a:
            return 1
        len_a = len(self.a)
        len_b = len(self.b)
        max_repeats = (len_b // len_a) + 2
        overlay = self.a
        for repeat in range(1, max_repeats + 1):
            if self.b in overlay:
                return repeat
            overlay += self.a
        return -1
    def public_Overlay_substring(self):
        return self.__private_Overlay_substring()

#--------------:
print(OS("xyz", "zxy").public_Overlay_substring() == 2)
print(OS("xyz", "xyzxyzxyz").public_Overlay_substring() == 3)
print(OS("xyz", "xyzxyzxyzxyz").public_Overlay_substring() == 4)
