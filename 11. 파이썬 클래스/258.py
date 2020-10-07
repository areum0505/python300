# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.gender))

    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
        
areum = Human("모름", 0, "모름")
areum.who()    

areum.setInfo("아름", 25, "여자")
areum.who() 
