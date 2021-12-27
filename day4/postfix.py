class Sym:
    OPEN_B = 1
    CLOSE_B = 2
    PLUS = 3
    MINUS = 4
    TIMES = 5
    DIVIDE = 6
    MOD = 7
    OPERAND = 8

class Expression:
    def __init__(self):
        self.stack = []
        self.size = 100
        self.expr = ""
        self.top = -1
    def eval_postfix(self):
        for sym in self.expr:
            print(sym, end=' ')
            sym_type = self.getSymtype(sym)
            if sym_type == Sym.OPERAND: self.push(int(sym))
            else:
                op2 = self.pop()
                op1 = self.pop()
                if sym_type == Sym.PLUS:
                    self.push(op1 + op2)
                elif sym_type == Sym.MINUS:
                    self.push(op1 - op2)
                elif sym_type == Sym.TIMES:
                    self.push(op1*op2)
                elif sym_type == Sym.DIVIDE:
                    self.push(op1 // op2)
                elif sym_type == Sym.MOD:
                    self.push(op1 % op2)
        return self.pop()
    
    def getSymtype(self, sym):
        if sym == '(' : sym_type = Sym.OPEN_B
        elif sym == ')' : sym_type = Sym.CLOSE_B
        elif sym == '+' : sym_type = Sym.PLUS
        elif sym == '-' : sym_type = Sym.MINUS
        elif sym == '*' : sym_type = Sym.TIMES
        elif sym == '/' : sym_type = Sym.DIVIDE
        elif sym == '%' : sym_type = Sym.MOD
        else: sym_type = Sym.OPERAND
        return sym_type
    def pop(self):
        return self.stack.pop()
    def push(self, data):
        self.stack.append(data)
    def isEmpty(self):
        return len(self.stack)==0
    def infix_postfix(self, expr):
        for token in expr:
            print(token, end=' ')
            # isalnum - 알파벳이나 수 operand
            if token.isalnum(): self.expr += token
            elif token=='(': self.push(token)
            elif token==')':
                sym = self.pop()
                while sym != '(':
                    self.expr += sym
                    sym = self.pop()
            else:
                # 스택 연산자 우선순위 비교함
                while not self.isEmpty() and\
                    self.precedence(self.stack[-1]) >= self.precedence(token):
                        sym=self.pop()
                        self.expr += sym
                self.push(token)
        while not self.isEmpty():
            self.expr += self.pop()
    def precedence(self, op):
        if op == '(' : return 0
        elif op in ['+', '-']: return 1
        elif op in ['*', '/', '%']: return 2

    
e = Expression()
expr = '9/(3+6-5)*7*(6-4)'
e.infix_postfix(expr)

print("수식 : ", e.expr)
print()
print("resulut = ", e.eval_postfix())
