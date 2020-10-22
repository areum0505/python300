# 다음과 같은 코드 구조를 사용하면 예외 발생 시 에러 메시지를 변수로 바인딩할 수 있습니다.

data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)
