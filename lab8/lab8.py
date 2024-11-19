class Account:
    def _init_(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transaction_history = []

    def check_balance(self):
        return f"Account Balance: {self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: {amount}")
            return f"{amount} deposited successfully."
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            return f"{amount} withdrawn successfully."
        return "Insufficient balance or invalid amount."

    def display_history(self):
        if not self.transaction_history:
            return "No transactions yet."
        return "\n".join(self.transaction_history)


class SavingsAccount(Account):
    def _init_(self, account_number, name, balance=0, withdrawal_limit=5000):
        super()._init_(account_number, name, balance)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            return f"Withdrawal failed. Limit is {self.withdrawal_limit}."
        return super().withdraw(amount)


class CheckingAccount(Account):
    def _init_(self, account_number, name, balance=0, overdraft_limit=1000):
        super()._init_(account_number, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew (overdraft allowed): {amount}")
            return f"{amount} withdrawn successfully."
        return "Exceeded overdraft limit."


# Example Usage:
savings = SavingsAccount(101, "Alice", 10000, 5000)
print(savings.deposit(2000))
print(savings.withdraw(6000))  # Exceeds withdrawal limit
print(savings.withdraw(4000))
print(savings.check_balance())
print(savings.display_history())

checking = CheckingAccount(102, "Bob", 2000, 1000)
print(checking.deposit(1000))
print(checking.withdraw(3500))  # Allows overdraft
print(checking.check_balance())
print(checking.display_history())