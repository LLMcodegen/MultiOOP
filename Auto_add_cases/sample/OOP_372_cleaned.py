
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LNS:
    def __init__(self, head_list):
        self.head = None
        current = None
        for val in head_list:
            new_node = Node(val)
            if not self.head:
                self.head = new_node
                current = self.head
            else:
                current.next = new_node
                current = current.next
class SN_LNS(LNS):
    def Larger_nodes(self):
        values = []
        current = self.head
        while current:
            values.append(current.val)
            current = current.next
        answer = [0] * len(values)
        stack = []
        for i, value in enumerate(values):
            while stack and value > values[stack[-1]]:
                idx = stack.pop()
                answer[idx] = value
            stack.append(i)
        return answer

#--------------:
print(SN_LNS([3, 8, 4, 1, 2]).Larger_nodes() == [8, 0, 0, 2, 0])
print(SN_LNS([6, 2, 4, 5, 3]).Larger_nodes() == [0, 4, 5, 0, 0])
print(SN_LNS([1, 3, 2, 4, 5]).Larger_nodes() == [3, 4, 4, 5, 0])
