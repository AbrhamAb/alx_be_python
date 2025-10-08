class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.
        Default balance is 0 if no initial balance is provided.
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Add the specified amount to the account balance.
        """
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        """
        Deduct the amount from account balance if funds are sufficient.
        Returns True if withdrawal was successful, False otherwise.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")