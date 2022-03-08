cm = int(input('''
고객님의 BIM지수를 알려드립니다. 
먼저 키를 입력해주세요.(cm 기준) >>>
'''))
kg = int(input('몸무게를 입력해주세요.>>>'))

bmi = kg/((cm*0.01)**2)

if bmi > 25:
    print('비만 체중입니다')

elif 18.5 <= bmi <= 25:
    print('정상 체중입니다.')

elif bmi < 18.5:
    print('저체중입니다.')