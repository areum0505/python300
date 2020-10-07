# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.gender))

areum = Human("아름", 25, "여자")
areum.who()
