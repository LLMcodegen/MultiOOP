
from fractions import Fraction
from itertools import product
from collections import defaultdict

class MNOOT:
    def __init__(self, x):
        self.x = x
class SN_MNOOT(MNOOT):
    def __init__(self, x, target):
        super().__init__(x)
        self.target = target
    def minimum_operators(self):
        max_n = 9
        x = self.x
        term_dict = defaultdict(list)
        for k in range(1, max_n + 1):
            ops_list = list(product(('*', '/'), repeat=k - 1))
            for ops in ops_list:
                expr = []
                num_ops = 0
                value = Fraction(x)
                expr.append(Fraction(x))
                valid = True
                for op in ops:
                    num_ops +=1
                    if op == '*':
                        expr.append('*')
                        expr.append(Fraction(x))
                        value *= Fraction(x)
                    elif op == '/':
                        expr.append('/')
                        expr.append(Fraction(x))
                        if x == 0:
                            valid = False
                            break
                        value /= Fraction(x)
                if valid:
                    term_dict[k].append((value, num_ops))
        min_ops_dict = {}
        for n in range(1, max_n +1):
            partitions = self.partitions(n)
            for partition in partitions:
                term_lists = [term_dict[k] for k in partition]
                term_combinations = list(product(*term_lists))
                for terms in term_combinations:
                    num_gaps = len(terms) -1
                    if num_gaps ==0:
                        ops_list = [()]
                    else:
                        ops_list = product(('+', '-'), repeat=num_gaps)
                    for ops in ops_list:
                        value = terms[0][0]
                        num_ops = terms[0][1]
                        valid = True
                        for i, op in enumerate(ops):
                            num_ops +=1
                            if op == '+':
                                value += terms[i+1][0]
                            elif op == '-':
                                value -= terms[i+1][0]
                            num_ops += terms[i+1][1]
                        if value not in min_ops_dict or num_ops < min_ops_dict[value]:
                            min_ops_dict[value] = num_ops
        target_value = Fraction(self.target)
        if target_value in min_ops_dict:
            return min_ops_dict[target_value]
        else:
            return -1
    def partitions(self, n, I=1):
        yield (n,)
        for i in range(I, n//2+1):
            for p in self.partitions(n - i, i):
                yield (i,)+p

#--------------:
print(SN_MNOOT(7, 343).minimum_operators() == 2)
print(SN_MNOOT(9, 81).minimum_operators() == 1)
print(SN_MNOOT(11, 1331).minimum_operators() == 2)
