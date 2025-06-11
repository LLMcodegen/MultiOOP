
class AOR:
    def __init__(self, s):
        self.s = s
class SN_AOR(AOR):
    def __init__(self, s):
        super().__init__(s)
    def Any_order(self):
        s = self.s.strip()[1:-1]
        n = len(s)
        results = []
        def generate_numbers(s_part):
            n = len(s_part)
            numbers = []
            if n == 1:
                return [s_part]
            if s_part[0] == '0':
                if s_part[-1] == '0':
                    return []
                else:
                    numbers.append("0." + s_part[1:])
                    return numbers
            if s_part[-1] == '0':
                return [s_part]
            numbers.append(s_part)
            for i in range(1, n):
                number = s_part[:i] + '.' + s_part[i:]
                numbers.append(number)
            return numbers
        for i in range(1, n):
            left = s[:i]
            right = s[i:]
            left_numbers = generate_numbers(left)
            right_numbers = generate_numbers(right)
            for ln in left_numbers:
                for rn in right_numbers:
                    coordinate = f"({ln}, {rn})"
                    results.append(coordinate)  
        return results

#--------------:
print(SN_AOR("(100)").Any_order() == ['(10, 0)'])
print(SN_AOR("(12)").Any_order() == ['(1, 2)'])