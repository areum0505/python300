# 192 번 문제의 결괏값을 result 이름의 리스트에 1차원 배열로 저장하라.

data = [
    [2000, 3050, 2050, 1980],
    [7500, 2050, 2050, 1980],
    [15450, 15050, 15550, 14900]
]

result = []

for i in data:
    for j in i:
        result.append(j * 1.00014)

print(result)
