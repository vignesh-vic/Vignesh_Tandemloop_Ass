class Calculator:
    def __init__(self, a, b, operation):
        self.a = float(a)
        self.b = float(b)
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        elif self.operation == 'divide':
            if self.b == 0:
                return 'Error: Division by zero is not allowed'
            return self.a / self.b
        else:
            return 'Error: Invalid operation'


add = Calculator(10.5, 5.2, 'add')
print(f'addition is {add.a} and {add.b}:',add.calculate())

sub = Calculator(1, 0, 'subtract')
print(f'subtract is {sub.a} and {sub.b} :', sub.calculate())

multiply=Calculator(10,1,"multiply")
print(f'multiply is {multiply.a} and {multiply.b} :',multiply.calculate())


divide=Calculator(10,1,"multiply")
print(f'division is {divide.a} and {divide.b} :',divide.calculate())
