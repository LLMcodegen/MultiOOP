
class BAR:
    def __init__(self, n):
        self.n = n
class SN_BAR(BAR):
    def Beautiful_array(self):
        def construct_beautiful_array(n):
            if n == 1:
                return [1]
            odd = construct_beautiful_array((n + 1) // 2)
            even = construct_beautiful_array(n // 2)
            return [2 * x - 1 for x in odd] + [2 * x for x in even]
        return construct_beautiful_array(self.n)

#--------------:
print(SN_BAR(1).Beautiful_array() == [1])
print(SN_BAR(2).Beautiful_array() == [1, 2])

