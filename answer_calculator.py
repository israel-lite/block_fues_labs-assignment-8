class Calculator:
    
    def add(self, num1, num2):
        return num1 + num2
    
    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Can not divied by 0"
        else:
            return num1 / num2


calc = Calculator()
print(calc.add(5, 3))        
print(calc.divide(10, 2)) 