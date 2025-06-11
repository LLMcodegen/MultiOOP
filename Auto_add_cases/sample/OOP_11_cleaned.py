class VLD_ST:
    def valid_string(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
#--------------:
print(VLD_ST().valid_string("([{}])") == True)
print(VLD_ST().valid_string("({[})]") == False)
print(VLD_ST().valid_string("{[]}()") == True)
