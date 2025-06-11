
class MT:
    def __init__(self, tasks, n):
        self.tasks = tasks
        self.n = n
    def __private_Minimum_time(self):
        from collections import Counter
        task_counts = Counter(self.tasks)
        max_freq = max(task_counts.values())
        max_freq_count = list(task_counts.values()).count(max_freq)
        min_time = (max_freq - 1) * (self.n + 1) + max_freq_count
        return max(min_time, len(self.tasks))
    def public_Minimum_time(self):
        return self.__private_Minimum_time()

#--------------:
print(MT(['A', 'B', 'C', 'D', 'E'], 1).public_Minimum_time() == 5)
print(MT(['A', 'A', 'B', 'B', 'C'], 3).public_Minimum_time() == 6)
print(MT(['A', 'A', 'A', 'B', 'C'], 2).public_Minimum_time() == 7)
