class BankAccount:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"تم إيداع ${amount}. الرصيد الحالي: ${self.balance}.")
        else:
            print("المبلغ يجب أن يكون أكبر من صفر.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"تم سحب ${amount}. الرصيد الحالي: ${self.balance}.")
        else:
            print("المبلغ غير صالح أو غير كافٍ.")

    def get_balance(self):
        return self.balance


# إنشاء مثيل وإجراء العمليات
account = BankAccount("1234", "جميل")
account.deposit(1000)
account.withdraw(500)
print(f"الرصيد الحالي: ${account.get_balance()}")


class SavingsAccount(BankAccount):
    # هذه الكلاس (Class) SavingsAccount تَرِث (Inherits) من كلاس BankAccount
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.0):
        # يتم تعيين قيم إضافية في  (Constructor) الخاص بكلاس SavingsAccount
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        # هذا هو تابع (Method) تطبيق الفائدة على الرصيد
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"تم تطبيق الفائدة. الرصيد الحالي: ${self.balance}")

    def __str__(self):
        # هذا هو تابع (Method) الطباعة المُعَدَّل الذي يطبع الرصيد والمعدل
        return f"الرصيد الحالي: ${self.balance} ، معدل الفائدة: {self.interest_rate * 100}%"


# إنشاء كائن (Instance) وإجراء العمليات
savings_account = SavingsAccount("5678", "أحمد", 1000, 0.05)
savings_account.apply_interest()
print(savings_account)