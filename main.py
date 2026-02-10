class Account:
    def __init__(self, acc_id, balance, name):
        self.acc_id = acc_id
        self.balance = balance
        self.name = name

    def get_acc_id(self):
        return self.acc_id

    def deposit(self, money):
        self._balance += self.balance

    def withdraw(self, money):
        if self._balance < money:
            return 0
        self._balance -= money
        return money

    def show_info(self):
        print(f"계좌 ID : {self._acc_id}")
        print(f"이름 : {self._name}")
        print(f"잔액 : {self._balance}\n")

acc_arr = []