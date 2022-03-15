class Food:
	favorite = "뿌링클"

a = Food()
b = Food()
print(a.favorite)
print(id(a.favorite))  #id() 함수로 메모리값 확인
print(b.favorite)
print(id(b.favorite))  #id() 함수로 메모리값 확인

# 값 바꾸기
Food.favorite = "황금올리브"

print(Food.favorite)
print(id(Food.favorite))

print(a.favorite)
print(id(a.favorite))  #id() 함수로 메모리값 확인
print(b.favorite)
print(id(b.favorite))  #id() 함수로 메모리값 확인