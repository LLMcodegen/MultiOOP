
class VS:
    def __init__(self, s):
        self.s = s
    def __private_Valid_String(self):
        open_brackets = 0
        stars = 0
        for char in self.s:
            if char == '(':
                open_brackets += 1
            elif char == ')':
                if open_brackets > 0:
                    open_brackets -= 1
                elif stars > 0:
                    stars -= 1
                else:
                    return False
            elif char == '*':
                stars += 1
        if open_brackets <= stars:
            return True
        else:
            return False
    def public_Valid_String(self):
        return self.__private_Valid_String()

#--------------:
print(VS("*)").public_Valid_String() == True)
print(VS("*").public_Valid_String() == True)
print(VS("((*").public_Valid_String() == False)
