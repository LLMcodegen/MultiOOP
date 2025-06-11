
class IAY:
    def __init__(self, arr):
        self.arr = arr

class SN_IAY(IAY):
    def Integer_array(self):
        n = len(self.arr)
        stack = []
        sum_min = 0
        prev_less = [0] * n
        next_less = [0] * n
        for i in range(n):
            while stack and self.arr[stack[-1]] >= self.arr[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)
        stack.clear()
        for i in range(n - 1, -1, -1):
            while stack and self.arr[stack[-1]] > self.arr[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)
        for i in range(n):
            left_count = i - prev_less[i]
            right_count = next_less[i] - i
            sum_min += self.arr[i] * left_count * right_count
        return sum_min

#--------------:
print(SN_IAY([1, 1, 1, 1, 1]).Integer_array() == 15)
print(SN_IAY([2, 2, 2, 2, 2]).Integer_array() == 30)
print(SN_IAY([1, 2, 3, 4, 5, 6]).Integer_array() == 56)
