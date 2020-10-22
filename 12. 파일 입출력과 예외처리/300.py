# 파이썬 예외처리는 다음과 같은 구조를 가질 수 있습니다.
# 아래의 코드에 대해서 예외처리를 사용하고 try, except, else, finally에 적당한 코드를 작성해봅시다. else와 finally는 적당한 문구를 print하시면 됩니다.

per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")
