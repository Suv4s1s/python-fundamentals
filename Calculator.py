class Calculator:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
    def mul(self,x,y):
        return x*y
    def div(self,x,y):
        return x/y
a=int(input("Enter first number: "))
b = int(input("Enter second number: "))
obj = Calculator()
print(obj.add(a,b))
print(obj.sub(a,b))
print(obj.mul(a,b))
print(obj.div(a,b))