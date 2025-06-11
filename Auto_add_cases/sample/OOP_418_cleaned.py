
class MBC:
    def __init__(self, s: str):
        self.s = s
class SN_MBC(MBC):
    def Match_Brace(self) -> str:
        stack = []
        current = []
        for char in self.s:
            if char == '(':
                stack.append(current)
                current = []
            elif char == ')':
                current.reverse()
                if stack:
                    current = stack.pop() + current
            else:
                current.append(char)
        return ''.join(current)

#--------------:
print(SN_MBC("(f(b(c)d)e)f").Match_Brace() == "ebcdff")
print(SN_MBC("(g(b(c)d)e)f").Match_Brace() == "ebcdgf")
print(SN_MBC("(h(b(c)d)e)f").Match_Brace() == "ebcdhf")
