
class DMM:
    def __init__(self, s):
        self.s = s
    def __private_Dictionary_minimum(self):
        last_occurrence = {char: i for i, char in enumerate(self.s)}
        stack = []
        seen = set()
        for i, char in enumerate(self.s):
            if char not in seen:
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    seen.remove(stack.pop())
                stack.append(char)
                seen.add(char)
        return ''.join(stack)
    def public_Dictionary_minimum(self):
        return self.__private_Dictionary_minimum()

#--------------:
print(DMM("aaaaa").public_Dictionary_minimum() == "a")
print(DMM("dcba").public_Dictionary_minimum() == "dcba")
print(DMM("abcabc").public_Dictionary_minimum() == "abc")
