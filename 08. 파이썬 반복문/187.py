# 리스트에 저장된 데이터를 아래와 같이 출력하라.

apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i[::-1]:
        print(j, "호")
