
class ASG:
    def __init__(self, a: int):
        self.a = a
class SN_ASG(ASG):
    def __init__(self, a: int, b: int):
        super().__init__(a)
        self.b = b
    def Any_string(self) -> str:
        result = []
        a_remaining = self.a
        b_remaining = self.b
        while a_remaining > 0 or b_remaining > 0:
            if (a_remaining > b_remaining):
                preferred = 'a'
                other = 'b'
                preferred_remaining = a_remaining
                other_remaining = b_remaining
            else:
                preferred = 'b'
                other = 'a'
                preferred_remaining = b_remaining
                other_remaining = a_remaining
            if len(result) >= 2 and result[-1] == result[-2] == preferred:
                if other_remaining > 0:
                    result.append(other)
                    if other == 'a':
                        a_remaining -= 1
                    else:
                        b_remaining -= 1
                else:
                    break
            else:
                result.append(preferred)
                if preferred == 'a':
                    a_remaining -= 1
                else:
                    b_remaining -= 1
        return ''.join(result)

#--------------:
print(SN_ASG(7, 1).Any_string() == "aabaa")
print(SN_ASG(3, 5).Any_string() == "bbabbaba")
print(SN_ASG(6, 2).Any_string() == "aabaabaa")
