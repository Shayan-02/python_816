class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw money from the account.

        Args:
            amount (int): The amount to withdraw.

        Returns:
            int: The new balance after withdrawal, or "Insufficient funds" if the
            account balance is not enough.
        """
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient funds"

    def get_balance(self):
        return self.balance


# Create a new bank account
account = BankAccount("123456789", 1000)

# Deposit money into the account
print(account.deposit(500))

# Withdraw money from the account
print(account.withdraw(200))

# Get the account balance
print(account.get_balance())
