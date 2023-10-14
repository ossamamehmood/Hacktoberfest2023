class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        elif amount > self.balance:
            return "Insufficient funds."
        else:
            return "Invalid withdrawal amount."

    def get_balance(self):
        return f"Account balance for {self.account_holder}: ${self.balance}"


def main():
    print("Welcome to the Banking System")
    account_holder = input("Enter your name: ")

    while True:
        try:
            initial_balance = float(input("Enter initial balance: "))
            user_account = BankAccount(account_holder, initial_balance)
            break  # Exit the loop if input is valid
        except ValueError:
            print("Invalid initial balance. Please enter a valid number.")

    while True:
        print("\nOptions:")
        print("Enter '1' to check balance")
        print("Enter '2' to make a deposit")
        print("Enter '3' to make a withdrawal")
        print("Enter '4' to exit")

        choice = input(": ")

        if choice == '1':
            print(user_account.get_balance())
        elif choice == '2':
            while True:
                try:
                    amount = float(input("Enter the deposit amount: "))
                    print(user_account.deposit(amount))
                    break  # Exit the loop if input is valid
                except ValueError:
                    print("Invalid deposit amount. Please enter a valid number.")
        elif choice == '3':
            while True:
                try:
                    amount = float(input("Enter the withdrawal amount: "))
                    print(user_account.withdraw(amount))
                    break  # Exit the loop if input is valid
                except ValueError:
                    print("Invalid withdrawal amount. Please enter a valid number.")
        elif choice == '4':
            print("Thank you for using the Banking System.")
            break
        else:
            print("Invalid input. Please enter a valid option.")


if __name__ == "__main__":
    main()
