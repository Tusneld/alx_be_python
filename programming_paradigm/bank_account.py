"""
0. Create a Simple Bank Account Class
Objective: Implement a BankAccount class that encapsulates banking operations.
"""

class BankAccount:
    """
    Represents a simple bank account with deposit, withdrawal, and balance display functionality.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes the BankAccount with an optional initial balance.

        :param initial_balance: The starting balance for the account (default is 0.0).
        """
        # Encapsulation: The account balance is an instance attribute.
        self.account_balance = initial_balance

    def deposit(self, amount: float):
        """
        Deposits the specified amount into the account.

        :param amount: The amount to deposit.
        """
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Withdraws the specified amount if funds are sufficient.

        :param amount: The amount to withdraw.
        :return: True if the withdrawal was successful, False otherwise.
        """
        if amount > 0 and self.account_balance >= amount:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")

# Note: The main-0.py script will import and test this class using command line arguments.