class LVPSS:
    def long_valid_substring(self, s: str) -> int:
        if not s:
            return 0
        stack = [-1]
        max_length = 0
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length
#--------------:
print(LVPSS().long_valid_substring("()(()") == 2)
print(LVPSS().long_valid_substring(")()())()()(") == 4)
print(LVPSS().long_valid_substring("((())()))()") == 8)