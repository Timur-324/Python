class BankAccount:
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = initial_balance
    
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
        elif amount <= 0:
            print("Сумма снятия должна быть положительной.")
        else:
            self.__balance -= amount
            print(f"Снятие {amount}...")

    def balance(self):
        return self.__balance

account = BankAccount('333', 'Садыков Тимур', 100000)

print(f"Создан счёт {account.account_number} владельца {account.owner}. Баланс: {account.balance()}")

account.deposit(10000)
print(f"Баланс: {account.balance()}")

account.withdraw(115000)

account.withdraw(50000)
print(f"Баланс: {account.balance()}")