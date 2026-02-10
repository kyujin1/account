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

def show_menu():
    print("메뉴")
    print("1. 계좌 생성")
    print("2. 입금")
    print("3. 출금")
    print("4. 계좌번호 전체 출력")
    print("5. 프로그램 종료")

def make_account():
    print("[계좌 생성]")
    try:
        acc_id = int(input("게좌 ID : (숫자로 입력)"))
        name = input("이름 : ")
        balance = int(input("입금액 : "))
        print()

    except ValueError:
        print("\n입력 형식이 올바르지 않습니다.\n")
        return

    acc_arr.append(Account(acc_id, balance, name))

def deposit_money():
    print("[입 금]")
    try:
        acc_id = int(input("계좌 ID : "))
        money = int(input("입금액 : "))
    except ValueError:
        print("\n입력 형식이 올바르지 않습니다.\n")
        return

    for acc in acc_arr:
        if acc.get_Acc_id() == acc_id:
            acc.deposit(money)
            print("입금 완료\n")
            return
    print("유효하지 않은 ID 입니다. \n")

def withdraw_money():
    print("[출 금]")
    try:
        acc_id = int(input("계좌 ID : "))
        money = int(input("출금액 : "))
    except ValueError:
        print("\n입력 형식이 올바르지 않습니다. \n")
        return

    for acc in acc_arr:
        if acc.get_Acc_id() == acc_id:
            if acc.withdraw(money) == 0:
                print("잔액 부족\n")
                return
            print("출금 완료\n")
            return
    print("유효하지 않은 ID 입니다.\n")

def show_acc_acc_info():
    for acc in acc_arr:
        acc.show_info()

