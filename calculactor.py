class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def add(self):
        return  self.a + self.b
   
    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b
   
    def div(self):
        if self.b != 0:
            return self.a/self.b
        else:
            return "Error: Division by zero!"

    def power(self):
        return self.a ** self.b if self.b != 0 else 1

    def gcd(self):
        x = self.a
        y = self.b
        while y != 0:
            x, y = y, x % y
        return abs(x)

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Введіть операцію (+, -, *, /, **, gcd): ")

calc = Calculator(a, b)

if operation == '+':
    print("Результат додавання:", calc.add())
elif operation == '-':
    print("Результат віднімання:", calc.sub())
elif operation == '*':
    print("Результат множення:", calc.mul())
elif operation == '/':
    print("Результат ділення:", calc.div())
elif operation == '**':
    print("Результат піднесення до степеня:", calc.power())
elif operation == 'nsd':
    print("Найбільший спільний дільник:", calc.gcd())
else:
    print("Невідома операція")