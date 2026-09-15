from savings_account import SavingsAccount
from checking_account import CheckingAccount


def main():
    # Create accounts
    savings = SavingsAccount("Rashid", 1000)
    checking = CheckingAccount("Rashid", 500)

    # Use accounts
    print(savings.account_type(), savings.balance)
    savings.deposit(200)
    savings.apply_interest()
    print("Savings after interest:", savings.balance)

    print(checking.account_type(), checking.balance)
    checking.withdraw(600)  # uses overdraft
    print("Checking after withdrawal:", checking.balance)


if __name__ == "__main__":
    main()
