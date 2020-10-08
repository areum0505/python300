# 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.

class Stock:
    def __init__(self, name, code, per, pbr, dividend_rate):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.dividend_rate = dividend_rate

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def get_name(self):
        return self.name

    def get_code(self):
        return self.code


삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
