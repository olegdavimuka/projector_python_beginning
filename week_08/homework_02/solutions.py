from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, account_number, holder_name, balance=0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    @abstractmethod
    def __str__(self):
        raise NotImplementedError("String representation must be implemented in subclasses.")


class CurrentAccount(Account):
    def __str__(self):
        return f"CurrentAccount(Account No: {self.account_number}, Holder: {self.holder_name}, Balance: {self.balance:.2f})"


class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0.0, interest_rate=0.02):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return (
            f"SavingsAccount(Account No: {self.account_number}, Holder: {self.holder_name}, "
            f"Balance: {self.balance:.2f}, Interest Rate: {self.interest_rate:.2%})"
        )


if __name__ == "__main__":
    accounts = [
        CurrentAccount("CA1001", "Alice", 1500.0),
        SavingsAccount("SA2001", "Bob", 2000.0, 0.03),
        CurrentAccount("CA1002", "Charlie", 500.0),
        SavingsAccount("SA2002", "Diana", 3000.0, 0.05),
    ]

    accounts[0].deposit(500)
    accounts[1].add_interest()
    accounts[2].withdraw(200)
    accounts[3].add_interest()

    for account in accounts:
        print(account)
