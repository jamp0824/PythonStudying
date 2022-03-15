class Calculator():
	def __init__(self, first, second):
		self.first = first
		self.second = second
	def add(self):
		result = self.first + self.second
		return result
	def minus(self):
		result = self.first - self.second
		return result	
	def multiple(self):
		result = self.first * self.second
		return result
	def divide(self):
		result = self.first / self.second
		return result

class PerfectCal(Calculator):
    def __init__(self, first, second):
        super().__init__(first, second)

    def modulo(self):
        result = self.first % self.second
        return result
    
    def divide(self):
        return self.first // self.second


a = PerfectCal(15,7)
b = Calculator(15,7)
# print(a.add())
# print(a.minus())
# print(a.multiple())
print(a.divide())
print(b.divide())
print(a.modulo())