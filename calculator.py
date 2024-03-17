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

    def lcm(self):
        return abs(self.a * self.b) // self.gcd()