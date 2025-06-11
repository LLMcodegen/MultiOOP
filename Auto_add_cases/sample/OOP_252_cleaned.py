
class CC:
    def __init__(self, s):
        self.s = s
    def __private_Change_Case(self):
        def backtrack(i, current):
            if i == len(self.s):
                result.append(current)
                return
            if self.s[i].isalpha():
                backtrack(i + 1, current + self.s[i].lower())
                backtrack(i + 1, current + self.s[i].upper())
            else:
                backtrack(i + 1, current + self.s[i])
        result = []
        backtrack(0, "")
        return result
    def public_Change_Case(self):
        return self.__private_Change_Case()

#--------------:
print(CC("a1").public_Change_Case() == ['a1', 'A1'])
print(CC("3z").public_Change_Case() == ['3z', '3Z'])
print(CC("12").public_Change_Case() == ['12'])
