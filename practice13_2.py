class Calculator:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    
    def add(self):
        return self.first + self.second

a = Calculator(6,3)
print(a.add())