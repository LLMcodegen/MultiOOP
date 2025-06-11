
class SID:
    def __init__(self, A):
        self.A = A
class SN_SID(SID):
    def start_index(self):
        A = self.A
        n = len(A)
        next_higher = [None] * n
        next_lower = [None] * n
        def make_monotonic_stack(sorted_indices):
            result = [None] * n
            stack = []
            for i in sorted_indices:
                while stack and i > stack[-1]:
                    result[stack.pop()] = i
                stack.append(i)
            return result
        next_higher = make_monotonic_stack(sorted(range(n), key=lambda i: (A[i], i)))
        next_lower = make_monotonic_stack(sorted(range(n), key=lambda i: (-A[i], i)))
        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True
        for i in range(n-2, -1, -1):
            if next_higher[i] is not None:
                odd[i] = even[next_higher[i]]
            if next_lower[i] is not None:
                even[i] = odd[next_lower[i]]
        return sum(odd)

#--------------:
print(SN_SID([1, 3, 2, 4, 5]).start_index() == 2)
print(SN_SID([1, 5, 2, 4, 3]).start_index() == 2)
print(SN_SID([1, 2, 3, 2, 1]).start_index() == 3)
