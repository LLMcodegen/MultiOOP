class VDPT:
    def valid_parentheses(self, n):
        if not isinstance(n, int) or n < 0:
            return False
        result = []
        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)
        backtrack("", 0, 0)
        return result
#--------------:
print(VDPT().valid_parentheses(5.1) == False)
print(VDPT().valid_parentheses(1.5) == False)
print(VDPT().valid_parentheses(3) == ['((()))', '(()())', '(())()', '()(())', '()()()'])
