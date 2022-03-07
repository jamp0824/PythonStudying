for i in range(10):
    print(i)

for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=" ")
    print('')

count = 0

while count<10:
    print(count)
    count+=1

    number = 0

    while True:
        print("문을 여시겠습니까? 1:Yes/2:No")
        number = int(input())

        if number == 1:
            print("문이 열렸습니다")
        elif number ==2:
            break