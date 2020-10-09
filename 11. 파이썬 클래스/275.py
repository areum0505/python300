# Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.

import random

class Account:
  account_count = 0

  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
    self.bank = "SC은행"

    num1 = random.randint(0, 999)
    num2 = random.randint(0, 99)
    num3 = random.randint(0, 999999)

    num1 = str(num1).zfill(3)  
    num2 = str(num2).zfill(2)   
    num3 = str(num3).zfill(6)   
    self.account_number = num1 + '-' + num2 + '-' + num3

    Account.account_count += 1

  @classmethod
  def get_account_num(cls):
    print(cls.account_count)

  def deposit(self, amount):
    if amount >= 1:
      self.balance += amount

  def withdraw(self, amount):
    if self.balance > amount:
      self.balance -= amount
