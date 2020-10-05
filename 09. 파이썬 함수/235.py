# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.

def convert_int(s):
    return int(s.replace(",", ""))


a = convert_int("1,234,567")
print(a, type(a))
