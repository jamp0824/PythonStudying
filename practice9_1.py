year = int(input('''안녕하세요! 연도를 입력하시면 윤년인지 판단해드립니다.
궁금한 연도를 입력해주세요. >>>'''))

if year % 4 == 0:
   
    if year % 100 != 0:
        print(f'{year}년은 윤년이 입니다.')

    elif year % 400 == 0:
        print(f'{year}년은 윤년입니다.')

    else:
        print(f'{year}년은 윤년이 아닙니다.')

else: 
    print(f'{year}년은 윤년이 아닙니다.')
