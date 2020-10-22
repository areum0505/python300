# 문자열로 표현된 PER 값을 실수로 변환한 후 이를 새로운 리스트에 저장해보세요.

per = ["10.31", "", "8.00"]
li = []

for i in per:
    try:
        v = float(i)
    except:
        v = 0
    li.append(v)

print(li)
