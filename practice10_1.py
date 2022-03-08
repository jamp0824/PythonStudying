#함수 미사용
print(3*100/20+345//2)
print(5*100/20+345//2)
print(7*100/20+345//2)
print(9*100/20+345//2)

#함수 사용
def Calculate(x):
    return x*100/20+345//2
print(Calculate(3))
print(Calculate(5))
print(Calculate(7))
print(Calculate(9))

def getSum(a,b):
    return a+b

num1 = 1
num2 = 2
result = getSum(num1,num2)
print(result)