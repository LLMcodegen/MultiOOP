
class DOT:
    def __init__(self, s):
        self.s = s
class SN_DOT(DOT):
    def __init__(self, s, k):
        super().__init__(s)
        self.k = k
    def Delete_Operation(self):
        stack = []
        for char in self.s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == self.k:
                    stack.pop()
            else:
                stack.append([char, 1])
        result = ''.join(char * count for char, count in stack)
        return result

#--------------:
print(SN_DOT("aabbcc", 5).Delete_Operation() == "aabbcc")
print(SN_DOT("aabbcc", 6).Delete_Operation() == "aabbcc")
print(SN_DOT("aabbcc", 7).Delete_Operation() == "aabbcc")
