# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

num1 = int(input("input number1: "))
num2 = int(input("input number2: "))
num3 = int(input("input number3: "))

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)
