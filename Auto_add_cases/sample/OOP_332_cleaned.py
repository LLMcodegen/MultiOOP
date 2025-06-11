
class ISK:
    def __init__(self, pushed):
        self.pushed = pushed
class SN_ISK(ISK):
    def __init__(self, pushed, popped):
        super().__init__(pushed)
        self.popped = popped
    def Initial_stack(self):
        stack = []
        pop_index = 0
        for value in self.pushed:
            stack.append(value)
            while stack and pop_index < len(self.popped) and stack[-1] == self.popped[pop_index]:
                stack.pop()
                pop_index += 1
        return pop_index == len(self.popped)

#--------------:
print(SN_ISK([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]).Initial_stack() == True)
print(SN_ISK([1, 2, 3, 4, 5], [1, 5, 4, 3, 2]).Initial_stack() == True)
print(SN_ISK([1, 2, 3, 4, 5], [1, 4, 2, 3, 5]).Initial_stack() == False)
