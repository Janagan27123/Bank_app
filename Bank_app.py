from datetime import datetime


with open("account.txt","w") as file:
    file.write('"admin":"UT010657"\n')
    file.write('"pass_word":"admin123"\n')


admin_data = {}
with open('account.txt', 'r') as file:
    for line in file:
        if ":" in line:
            key, value = line.strip().split(":")
            admin_data[key.strip('"')] = value.strip('"')

    while True:
     user_id = input("User Id : ")
     pass_word = input("Password : ")
     if user_id == admin_data.get("admin") and pass_word == admin_data.get("pass_word"):
        print("Login successfully")
        break
     else:
        print("Invalid userId or Password")
       

user_account = {}
next_account_number = 15001


def create_account():
    global next_account_number
    name = input("Enter account user name: ")
    try:
        initial_balance = float(input("Enter the amount: "))
        if initial_balance < 0:
            print("Invalid amount")
            return
    except ValueError:
        print("Invalid amount entered.")
        return

    while True:
        password = input("Create new password (min 6 characters): ")
        if len(password) < 6:
            print("Password too short. Please enter at least 6 characters.")
        else:
            break

    account_number = next_account_number
    next_account_number += 1

    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_account[account_number] = {
        "name": name,
        "balance": initial_balance,
        "transactions": [(f"Initial Deposit on {date}", initial_balance)],
        "password": password
    }

    with open("account.txt", "a") as file:
       file.write(f"{account_number}:{user_account[account_number]}\n")
       
    print(f"Account created successfully. your Account Number is: {account_number}")


   
def deposit():
    try:
        account_number = int(input("Enter account number: "))
        password = input("Enter your password: ")
        
        if account_number not in user_account or user_account[account_number]["password"] != password:
           print("Account not found or incorrect password.")
           return

        amount = float(input("Enter amount to deposit: "))
        if amount < 0:
            print("Amount must be positive.")
            return

        user_account[account_number]["balance"] += amount
        
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_account[account_number]["transactions"].append((f"Deposit on {date}", amount))
        print("Deposit successful.")

    except ValueError:
        print("Invalid input.")

def withdraw_money():
    try:
        account_number = int(input("Enter account number: "))
        password = input("Enter your password: ")

        
        if account_number not in user_account or user_account[account_number]["password"] != password:
           print("Account not found or incorrect password.")
           return
            
        amount = float(input("Enter amount to withdraw: "))
        
        
        if amount < 0:
           print("Invalid amount.")
           return
        if amount > user_account[account_number]["balance"]:
           print("Insufficient balance.")
           return


        user_account[account_number]["balance"] -= amount
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_account[account_number]["transactions"].append((f"Withdrawal on {date}", amount))
        print("Withdrawal successful.")

    except ValueError:
        print("Invalid input.")
def balance():
    try:
        account_number = int(input("Enter the account number: "))
        if account_number not in user_account:
            print("invalid account number")
            return
        print(f"current balance: {user_account[account_number]['balance']:.2f}")
    except ValueError:
        print("invalid input")


def Transaction():
    try:
        account_number = int(input("Enter the account number: "))
        if account_number not in user_account:
            print("invalid account number")
            return
        for history, amount in user_account[account_number]["transactions"]:
            print(f"{history}: {amount:.2f}")
        
    except ValueError:
        print("invalid input")


def main():
    while True:
        print(
              "*****MENU*****\n"
              "1. create account\n"
              "2. deposit money\n"
              "3. withdraw money\n"
              "4. check balance\n"
              "5. transaction history\n"
              "6. exit\n"
              "**************\n"
            )
        choice = input("enter your choice (1-6) : ")

        
        if choice == "1":
          create_account()
        elif choice =="2":
          deposit()
        elif choice =="3":
          withdraw_money()
        elif choice == "4":
          balance()
        elif choice == "5":
          Transaction()
        elif choice == "6":
          print("good bye.")
          break
        else:
          print("invalid choice. please select number 1-6")
    

if __name__ == "__main__":
    main()

 




