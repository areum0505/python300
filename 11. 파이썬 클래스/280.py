# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.

import random

class Account:
  account_count = 0

  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
    self.bank = "SC은행"
    self.deposit_count = 0
    self.deposit_log = []
    self.withdraw_log = []

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
    self.deposit_log.append(amount)
    if amount >= 1:
      self.balance += amount

    self.deposit_count += 1
    if self.deposit_count % 5 == 0:
      self.balance = (self.balance * 1.01)

  def withdraw(self, amount):
    if self.balance > amount:
      self.withdraw_log.append(amount)
      self.balance -= amount

  def display_info(self):
    print("은행이름: " + self.bank)
    print("예금주: " + self.name)
    print("계좌번호: " +  self.account_number)
    print("잔고: " + format(self.balance, ",") + "원")

  def withdraw_history(self):
    for amount in self.withdraw_log:
      print(amount)

  def deposit_history(self):
    for amount in self.deposit_log:
      print(amount)
