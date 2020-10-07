# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


areum = Human("조아름", 25, "여자")
print("이름:", areum.name, "나이:", str(areum.age), "성별:", areum.gender)
