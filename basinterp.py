from basparse import *

class Interpreter:
    def __init__(self):
        self.env = {}

    def run(self, node):
        if isinstance(node, Program):
            for s in node.statements:
                self.run(s)

        elif isinstance(node, Block):
            for s in node.statements:
                self.run(s)

        elif isinstance(node, Assign):
            val = self.run(node.expr)
            name = node.var

            if node.op == '=':
                self.env[name] = val
            elif node.op == '+=':
                self.env[name] += val
            elif node.op == '-=':
                self.env[name] -= val
            elif node.op == '*=':
                self.env[name] *= val
            elif node.op == '/=':
                self.env[name] /= val
            elif node.op == '%=':
                self.env[name] %= val
            elif node.op == '.=':
                self.env[name] = str(self.env.get(name, "")) + str(val)

        elif isinstance(node, If):
            if self.run(node.cond):
                self.run(node.then_body)
            elif node.else_body:
                self.run(node.else_body)

        elif isinstance(node, While):
            while self.run(node.cond):
                self.run(node.body)

        elif isinstance(node, Echo):
            print(self.run(node.expr), end='')

        elif isinstance(node, Print):
            print(self.run(node.expr), end='')

        elif isinstance(node, BinOp):
            l = self.run(node.left)
            r = self.run(node.right)
            op = node.op

            if op == '+': return l + r
            if op == '-': return l - r
            if op == '*': return l * r
            if op == '/': return l / r
            if op == '%': return l % r
            if op == '.': return str(l) + str(r)
            if op == '!=': return l != r
            if op == '>': return l > r
            if op == '>=': return l >= r
            if op == '<': return l < r
            if op == '<=': return l <= r

        elif isinstance(node, Number):
            return node.value

        elif isinstance(node, String):
            return node.value

        elif isinstance(node, Variable):
            return self.env.get(node.name, 0)
