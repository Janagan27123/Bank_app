import json
import os
from datetime import datetime

DATA_FILE = "accounts.json" 

# Load or initialize data
def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": {}, "admin": {"username": "UT010657", "password": "admin123"}}
    with open(DATA_FILE, "r") as file:
        return json.load(file)
    
def save_data(data):
        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
    
    
        
def create_account(data):
    username = input("Enter new username: ")
    if username in data["users"]:
        print("Username already exists.")
        return
    password = input("Enter password: ")
    data["users"][username] = {
        "password": password,
        "balance": 0.0,
        "transactions": []
    }
    save_data(data)
    print("Account created successfully.")

def view_all_accounts(data):
    print("\n--- All User Accounts ---")
    for user in data["users"]:
        print(f"Username: {user}, Balance: ${data['users'][user]['balance']:.2f}")
    print("-------------------------")

def user_menu(username, data):
    while True:
        print("\n1. View Balance\n2. Deposit\n3. Withdraw\n4. Transaction History\n5. Logout")
        choice = input("Choose an option: ")

        user = data["users"][username]

        if choice == '1':
            print(f"Your balance is: ${user['balance']:.2f}")
        elif choice == '2':
            amount = float(input("Enter deposit amount: "))
            user["balance"] += amount
            user["transactions"].append(
                {"type": "Deposit", "amount": amount, "time": str(datetime.now())}
            )
            save_data(data)
            print("Deposit successful.")
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: "))
            if amount > user["balance"]:
                print("Insufficient funds.")
            else:
                user["balance"] -= amount
                user["transactions"].append(
                    {"type": "Withdrawal", "amount": amount, "time": str(datetime.now())}
                )
                save_data(data)
                print("Withdrawal successful.")
        elif choice == '4':
            print("\n--- Transaction History ---")
            for t in user["transactions"]:
                print(f"{t['time']} - {t['type']}: ${t['amount']:.2f}")
        elif choice == '5':
            break
        else:
            print("Invalid option.")

def login(data):
    username = input("Username: ")
    password = input("Password: ")

    if username == data["admin"]["username"] and password == data["admin"]["password"]:
        while True:
            print("\nAdmin Menu:\n1. Create User Account\n2. View All Accounts\n3. Logout")
            choice = input("Choose an option: ")
            if choice == '1':
                create_account(data)
            elif choice == '2':
                view_all_accounts(data)
            elif choice == '3':
                break
            else:
                print("Invalid option.")
    elif username in data["users"] and data["users"][username]["password"] == password:
        user_menu(username, data)
    else:
        print("Invalid login.")

def main():
    data = load_data()
    #attemts=0
    while True:
        print("\n--- Mini ATM Bank App ---")
        print("1. Login\n2. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            #while attemts < 3:
                login(data)
                '''break
            else:
                print("Too many failed attemts.Exiting.")
                break'''

        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()

 




