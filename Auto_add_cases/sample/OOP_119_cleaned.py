
class INT:
    def __init__(self, s):
        self.s = s
    def __private_Integer_nesting(self):
        s = self.s
        index = 0
        def parse():
            nonlocal index
            if index >= len(s):
                return None
            if s[index] == '[':
                index += 1
                lst = []
                while index < len(s) and s[index] != ']':
                    if s[index] == ',':
                        index += 1
                    else:
                        lst.append(parse())
                index += 1
                return lst
            else:
                is_negative = False
                if s[index] == '-':
                    is_negative = True
                    index += 1
                num = 0
                while index < len(s) and s[index].isdigit():
                    num = num * 10 + int(s[index])
                    index += 1
                return -num if is_negative else num
        return parse()
    def public_Integer_nesting(self):
        return self.__private_Integer_nesting()

#--------------:
print(INT("[[12],[34,56],78]").public_Integer_nesting() == [[12], [34, 56], 78])
print(INT("[-10,-20,-30]").public_Integer_nesting() == [-10, -20, -30])
print(INT("[[1],2,3,[4,5]]").public_Integer_nesting() == [[1], 2, 3, [4, 5]])
