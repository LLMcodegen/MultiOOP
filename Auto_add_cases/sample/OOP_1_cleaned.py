class MNS:
    def __init__(self, machines):
        self.machines = machines
    def __private_Ministeps(self) -> int:
        total_clothes = sum(self.machines)
        n = len(self.machines)
        if total_clothes % n != 0:
            return -1
        target = total_clothes // n
        max_steps = 0
        cumulative_balance = 0
        for clothes in self.machines:
            balance = clothes - target
            cumulative_balance += balance
            max_steps = max(max_steps, abs(cumulative_balance), balance)
        return max_steps
    def public_Ministeps(self) -> int:
        return self.__private_Ministeps()

#--------------:
print(MNS([0, 4, 4, 0]).public_Ministeps() == 2)
print(MNS([3, 1, 2, 0]).public_Ministeps() == -1)
print(MNS([10, 0, 0, 10]).public_Ministeps() == 5)
