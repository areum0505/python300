# 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.

my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(my_list[i+1] - my_list[i])
