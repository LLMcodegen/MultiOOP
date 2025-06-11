
class FEQ:
    def __init__(self, num: str):
        self.num = num
class SN_FEQ(FEQ):
    def Fibonacci_equation(self):
        def dfs(index, path):
            if index == len(self.num) and len(path) >= 3:
                return path
            for i in range(index + 1, len(self.num) + 1):
                if self.num[index] == '0' and i > index + 1:
                    break
                num_part = int(self.num[index:i])
                if num_part >= 2**31:
                    break
                if len(path) >= 2 and path[-1] + path[-2] < num_part:
                    break
                if len(path) < 2 or path[-1] + path[-2] == num_part:
                    result = dfs(i, path + [num_part])
                    if result:
                        return result
            return []
        return dfs(0, [])

#--------------:
print(SN_FEQ("11235813").Fibonacci_equation() == [1, 1, 2, 3, 5, 8, 13])
print(SN_FEQ("1001").Fibonacci_equation() == [])
print(SN_FEQ("123581321").Fibonacci_equation() == [1, 2, 3, 5, 8, 13, 21])
