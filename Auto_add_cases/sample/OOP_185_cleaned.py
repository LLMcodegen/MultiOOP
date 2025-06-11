
class IS:
    def __init__(self, s):
        self.s = s
    def __private_Invert_String(self):
        words = self.s.split(' ')
        reversed_words = [word[::-1] for word in words]
        reversed_string = ' '.join(reversed_words)
        return reversed_string
    def public_Invert_String(self):
        return self.__private_Invert_String()

#--------------:
print(IS("Goodbye world").public_Invert_String() == "eybdooG dlrow")
print(IS("This is a test").public_Invert_String() == "sihT si a tset")
print(IS("Keep coding").public_Invert_String() == "peeK gnidoc")