
class BLS:
    def __init__(self, expression: str):
        self.expression = expression
class SN_BLS(BLS):
    def Booleans(self):
        return self.evaluate(self.expression)
    def evaluate(self, expr: str):
        if expr == 't':
            return True
        elif expr == 'f':
            return False
        elif expr.startswith('!'):
            return not self.evaluate(expr[2:-1])
        elif expr.startswith('&'):
            sub_expressions = self.extract_sub_expressions(expr[2:-1])
            return all(self.evaluate(sub_expr) for sub_expr in sub_expressions)
        elif expr.startswith('|'):
            sub_expressions = self.extract_sub_expressions(expr[2:-1])
            return any(self.evaluate(sub_expr) for sub_expr in sub_expressions)
        else:
            raise ValueError(f"Invalid expression: {expr}")
    def extract_sub_expressions(self, expr: str):
        sub_expressions = []
        depth = 0
        current_sub_expr = []
        for char in expr:
            if char == ',' and depth == 0:
                sub_expressions.append(''.join(current_sub_expr))
                current_sub_expr = []
            else:
                if char == '(':
                    depth += 1
                elif char == ')':
                    depth -= 1
                current_sub_expr.append(char)
        if current_sub_expr:
            sub_expressions.append(''.join(current_sub_expr))
        return sub_expressions

#--------------:
print(SN_BLS("&(!(t),f)").Booleans() == False)
print(SN_BLS("|(!(f),f)").Booleans() == True)
print(SN_BLS("&(|(f,t),t)").Booleans() == True)
