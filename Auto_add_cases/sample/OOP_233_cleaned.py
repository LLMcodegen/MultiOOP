
class TR:
    def __init__(self, temperatures):
        self.temperatures = temperatures
    def __private_Temperature_rise(self):
        n = len(self.temperatures)
        answer = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and self.temperatures[i] >= self.temperatures[stack[-1]]:
                stack.pop()
            if stack:
                answer[i] = stack[-1] - i
            stack.append(i)
        return answer
    def public_Temperature_rise(self):
        return self.__private_Temperature_rise()

#--------------:
print(TR([50, 50, 50, 50]).public_Temperature_rise() == [0, 0, 0, 0])
print(TR([50, 50, 50, 50, 50]).public_Temperature_rise() == [0, 0, 0, 0, 0])
print(TR([50, 50, 50, 50, 50, 50]).public_Temperature_rise() == [0, 0, 0, 0, 0, 0])
