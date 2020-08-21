# 아래 코드의 실행 결과를 예상해보세요.
lang = 'python'
lang[0] = 'P'
print(lang)
# Traceback (most recent call last):
#   File "C:/Users/User/PycharmProjects/2206Python/test.py", line 3, in <module>
#     lang[0] = 'P'
# TypeError: 'str' object does not support item assignment
# 문자열은 수정할 수 없습니다. 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.
