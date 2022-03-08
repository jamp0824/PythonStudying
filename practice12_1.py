example_tupleOne=(1,2)
example_tupleTwo=("python",2,5)
example_tupleThree=(0,4,(1,2,3))

#print(example_tupleOne)
#print(example_tupleTwo)
#print(example_tupleThree)

plus_tuple = example_tupleOne + example_tupleTwo
print(plus_tuple)
multi_tuple = example_tupleTwo*2
print(multi_tuple)

def minmax(ex_list):
    return min(ex_list), max(ex_list)

ex_list=[1,2,3,4,5]
result_tuple = minmax(ex_list)

print(result_tuple)

setOne = {1,2,3}
setTwo = set([7,6,5,4,1])
setThree = set("Hello World")

print(setOne)
print(setTwo)
print(setThree)

setOne = {1,2,3}
setTwo = {2,3,4}

print(setOne & setTwo)
print(setOne.intersection(setTwo))

print('setOne | setTwo = ',setOne | setTwo)
print('setOne.union(setTwo) = ',setOne.union(setTwo))

print('setOne - setTwo = ', setOne-setTwo)
print('setOne.difference(setTwo) = ',setOne.difference(setTwo))

setOne.add(5)
print('setOne.add(5) = ' ,end="")
print(setOne)
setTwo.update([9,8,7])
print('setTwo.update([9,8,7] = ',end="")
print(setTwo)
setTwo.remove(7)
print(setTwo)


