
class VSR:
    def __init__(self, s):
        self.s = s
    def __private_Valid_string(self):
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                if count < 0:
                    return False
            return count == 0
        from collections import deque
        queue = deque([self.s])
        visited = set([self.s])
        valid_results = []
        found = False
        while queue:
            current_string = queue.popleft()
            if is_valid(current_string):
                valid_results.append(current_string)
                found = True
            if found:
                continue
            for i in range(len(current_string)):
                if current_string[i] not in ('(', ')'):
                    continue
                new_string = current_string[:i] + current_string[i+1:]
                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)
        return valid_results if valid_results else [""]
    def public_Valid_string(self):
        return self.__private_Valid_string()

#--------------:
print(VSR("(())(()").public_Valid_string() == ["(())()"])
print(VSR("(a)()").public_Valid_string() == ["(a)()"])
print(VSR("()())()").public_Valid_string() == ["(())()", "()()()"])
