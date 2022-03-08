example_list = [1,2,3,4,5,6,7,8,9,10]

sliceOne = example_list[0:5]
sliceTwo = example_list[5:10]
sliceThree = example_list[:5] #list[ : b]는 0부터 인덱스 b의 값까지,
sliceFour = example_list[5:]  #list[a : ]는 인덱스 a부터 리스트의 끝까지로 인식돼요.

#print(example_list)
print(sliceOne)
print(sliceTwo)
print(sliceThree)
print(sliceFour)

example_list.append(10)
print(example_list)

example_list.insert(9,11)
print(example_list)

del example_list[10]
print(example_list)

example_list.remove(10)
print(example_list)