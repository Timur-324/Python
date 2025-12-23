class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0, limit=200000):
        self.account_number = account_number
        self.owner = owner
        self.__balance = initial_balance
        self.__limit = limit
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение на {amount}...")
        else:
            print("Сумма пополнения должна быть положительной.")
    
    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Попытка снять {amount}...")
            print(f"Ошибка: недостаточно средств для снятия {amount}. Баланс: {self.__balance}")
        elif amount > self.__limit:
            print(f"Попытка снять {amount}...")
            print(f"Ошибка: превышение лимита операции (лимит = {self.__limit})")
        elif amount <= 0:  
            print("Сумма снятия должна быть положительной.")
        else:
            self.__balance -= amount
            print(f"Снятие {amount}...")

    def balance(self):
        return self.__balance
    
    @property
    def limit(self):
        return self.__limit
    
    @limit.setter
    def limit(self, value):

        if value <= 0:
            print("Лимит должен быть положительным числом!")
        else:
            self.__limit = value
            print(f"Установлен лимит снятия: {self.__limit}")   

account = BankAccount('333', 'Садыков Тимур', 100000)

print(f"Создан счёт {account.account_number} владельца {account.owner}. Баланс: {account.balance()}")

account.limit = 10000

account.withdraw(15000)

account.withdraw(3333)
print(f"Баланс: {account.balance()}")