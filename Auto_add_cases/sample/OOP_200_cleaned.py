
class SE:
    def __init__(self, equation):
        self.equation = equation
    def __private_solve_equation(self):
        left, right = self.equation.split('=')
        def parse(expression):
            x_coef = 0
            const_sum = 0
            sign = 1
            i = 0
            while i < len(expression):
                if expression[i] == '+':
                    sign = 1
                    i += 1
                elif expression[i] == '-':
                    sign = -1
                    i += 1
                else:
                    num_start = i
                    while i < len(expression) and expression[i].isdigit():
                        i += 1
                    if i < len(expression) and expression[i] == 'x':
                        num = expression[num_start:i]
                        if num == '' or num == '+':
                            x_coef += sign * 1
                        elif num == '-': 
                            x_coef += sign * -1
                        else:
                            x_coef += sign * int(num)
                        i += 1
                    else:
                        num = expression[num_start:i]
                        const_sum += sign * int(num)
            return x_coef, const_sum
        left_x_coef, left_const_sum = parse(left)
        right_x_coef, right_const_sum = parse(right)
        x_coef = left_x_coef - right_x_coef
        const_sum = right_const_sum - left_const_sum
        if x_coef == 0:
            if const_sum == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            if const_sum % x_coef == 0:
                return f"x={const_sum // x_coef}"
            else:
                return "No solution"
    def public_solve_equation(self):
        return self.__private_solve_equation()

#--------------:
print(SE("x+4-x=10").public_solve_equation() == "No solution")
print(SE("7x=2x+15").public_solve_equation() == "x=3")
print(SE("3x+1=x+8").public_solve_equation() == "No solution")
