# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
t = (1, 2, 3)
t[0] = 'a'
# Traceback (most recent call last):
#   File "D:/Python/python2학년/basic/test.py", line 3, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

# tuple은 원소(element)의 값을 변경할 수 없습니다.
