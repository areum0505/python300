# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.

def printmxn(s, n):
    for i in range(int(len(s) / n) + 1):
        print(s[i * n:i * n + n])


printmxn("아이엠어보이유알어걸", 3)
