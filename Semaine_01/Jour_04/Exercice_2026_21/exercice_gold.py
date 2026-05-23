class BankAccount:

    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
        else:
            raise Exception("Authentication failed")

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated")

        if amount <= 0:
            raise Exception("Deposit must be a positive number")

        self.balance += amount

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("User not authenticated")

        if amount <= 0:
            raise Exception("Withdrawal must be a positive number")

        if amount > self.balance:
            raise Exception("Insufficient funds")

        self.balance -= amount