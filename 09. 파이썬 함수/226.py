# 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.

def print_5xn(s):
    for i in range(int(len(s) / 5) + 1):
        print(s[i * 5:i * 5 + 5])


print_5xn("아이엠어보이유알어걸")
