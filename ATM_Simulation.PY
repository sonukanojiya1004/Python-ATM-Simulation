import json

def save_accounts():
    with open("accounts.json", "w") as file:
        json.dump(Accounts, file, indent=4)

def load_accounts():
    try:
        with open("accounts.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}





Accounts = load_accounts()
for account in Accounts.values():

    account.setdefault('transactions', [])

def check_balance(card_number):
    balance = Accounts[card_number]['balance']
    print(f"Your current balance is: ${balance:.2f}")

def deposit_money(card_number):
    amount = float(input("Enter the amount to deposit: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
        return

    Accounts[card_number]['balance'] += amount
    transaction = {
    'type': 'Deposit',
    'amount': amount,
    'balance': Accounts[card_number]['balance']
    }

    Accounts[card_number]['transactions'].append(transaction)
    print(f"${amount:.2f} deposited successfully.")
    save_accounts()

def withdraw_money(card_number):
    amount = float(input("Enter the amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
        return

    if amount > Accounts[card_number]['balance']:
        print("Insufficient balance.")
        return

    Accounts[card_number]['balance'] -= amount
    transaction = {
    'type': 'Withdrawal',
    'amount': amount,
    'balance': Accounts[card_number]['balance']
    }

    Accounts[card_number]['transactions'].append(transaction)
    print(f"${amount:.2f} withdrawn successfully.")
    save_accounts()


def mini_statement(card_number):
    transactions = Accounts[card_number]['transactions']
    if not transactions:
        print("No transactions found.")
        return

    print("\n=====Mini Statement=====")
    for transaction in transactions[-5:]:
        print(f"{transaction['type']}: ${transaction['amount']:.2f} | Balance: ${transaction['balance']:.2f}")

def transactions_history(card_number):
    transactions = Accounts[card_number]['transactions']
    if not transactions:
        print("No transactions found.")
        return

    print("\n=====Transactions History=====")
    for transaction in transactions:
        print(f"{transaction['type']}: ${transaction['amount']:.2f} | Balance: ${transaction['balance']:.2f}")


def Dashboard(card_number):
    while True:
        print(f"\n=====WELCOME {Accounts[card_number]['name']} =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Transactions History")
        print("6. Logout")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance(card_number)
        elif choice == 2:
            deposit_money(card_number)
        elif choice == 3:
            withdraw_money(card_number)
        elif choice == 4:
            mini_statement(card_number)
        elif choice == 5:
            transactions_history(card_number)
        elif choice == 6:
            print("Logging out...")
            break

        else:
            print("Invalid choice. Please try again.")

def create_account():
     card_number = input("Enter your card number: ")

     if card_number in Accounts:
         print("Account already exists!")
         return

     name = input("Enter your name: ")
     pin = input("Enter your 4-digit PIN: ")
     balance = float(input("Enter initial balance: "))
     Transactions = []

     Accounts[card_number] = {
         'name': name,
         'pin': pin,
         'balance': balance,
         'transactions': Transactions
     }

     print("Account created successfully!")
     save_accounts()

def login():
    card_number = (input("Enter your card number: "))
    pin = input("Enter your PIN: ")
    
    if card_number in Accounts and Accounts[card_number]['pin'] == pin:
        print("Login successful!")
        Dashboard(card_number)
    else:
        print("Invalid card number or PIN.")
        return None





while True:
    print("=====WELCOME TO ATM=====")

    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
            create_account()
    elif choice == 2:
            login()
    elif choice == 3:
            print("Thank you for using our ATM!")
            break
    else:
            print("Invalid choice. Please try again.")

