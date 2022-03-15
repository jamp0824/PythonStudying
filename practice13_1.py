class Calculator:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
        
a = Calculator()
a.setdata(6,3)

print(a.add())
#b = Calculator()
#b.setdata(10,7)
#print(b.first)
#print(b.second)