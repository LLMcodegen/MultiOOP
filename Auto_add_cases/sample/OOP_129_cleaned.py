
class SNU:
    def __init__(self, num: str, k: int):
        self.num = num
        self.k = k
    def __private_smallest_number(self) -> str:
        num = list(self.num)
        stack = []
        for digit in num:
            while self.k > 0 and stack and stack[-1] > digit:
                stack.pop()
                self.k -= 1
            stack.append(digit)
        if self.k > 0:
            stack = stack[:-self.k]
        return ''.join(stack).lstrip('0') or '0'
    def public_smallest_number(self) -> str:
        return self.__private_smallest_number()

#--------------:
print(SNU("10001", 2).public_smallest_number() == "0")
print(SNU("7654321", 3).public_smallest_number() == "4321")
print(SNU("54321", 2).public_smallest_number() == "321")
