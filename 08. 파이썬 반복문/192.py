# 191번의 출력 결과에 행단위로 "----" 구분자를 추가하라.

data = [
    [2000, 3050, 2050, 1980],
    [7500, 2050, 2050, 1980],
    [15450, 15050, 15550, 14900]
]

for i in data:
    for j in i:
        print(j * 1.00014)
    print("-" * 4)
