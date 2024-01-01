class ATM:
    def __init__(self):
        self.accounts = {}  # Store account balances

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with an initial balance of {initial_balance}")
        else:
            print(f"Account {account_number} already exists. Please choose another account number.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]
            print(f"Your balance is: {balance}")
        else:
            print("Account not found. Please check your account number.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited {amount}. Your new balance is: {self.accounts[account_number]}")
        else:
            print("Account not found. Please check your account number.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]:
                self.accounts[account_number] -= amount
                print(f"Withdrew {amount}. Your new balance is: {self.accounts[account_number]}")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found. Please check your account number.")

    def exit_atm(self):
        print("Exiting ATM. Thank you!")

def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            atm.create_account(account_number, initial_balance)

        elif choice == "2":
            account_number = input("Enter account number: ")
            atm.check_balance(account_number)

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            atm.deposit(account_number, amount)

        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(account_number, amount)

        elif choice == "5":
            atm.exit_atm()
            break

        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()
