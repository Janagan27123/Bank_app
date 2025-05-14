import json
import os
from datetime import datetime

Data_File = "accounts.json"


def load_data():
    if not os.path.exists(Data_File):
        return{"users":{},"admin":{"username":"UT010657","password":"Admin@123"}}
    with open(Data_File,"r")as file:
        return json.load(file)
    

def save_data(data):
    with open(Data_File,'w')as file:
        json.dump(data,file,indent=4)


def create_account(data):
    username=input("Enter new username:")
    if username in data["users"]:
        print("username already exists.")
        return
    password=input("enter password:")
    data["users"][username]={
        "password":password,
        "balance":0.0,
        "transactions":[]
    }
    save_data(data)
    print("account created successfuly.")

def view_all_accounts(data):
    print("\n***All User Accounts***")
    for user in data["users"]:
        print(f"Username:{user}, Balance: ${data['users'][user]['balance']:.2f}")
        print("***********************")

def user_menu(username,data):
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("choose an option:")

        user = data["users"][username]

        if choice == '1':
            print(f"Your balance is: ${user}['balance]:.2f")

        elif choice == '2':
            amount = float(input("Enter Deposit Amount:"))
            user["balance"]+=amount
            user["transactions"].append(
                {"type":"Deposit","amount":amount,"time":str(datetime.now())}
            )
            save_data(data)
            print("Deposit successful.")
        
        elif choice == '3':
            amount = float(input("Enter Withdraw Amount:"))
            if amount>user["balance"]:
                print("Insufficient funds.")
            else:
                user["balance"]-=amount
                user["transactions"].append(
                {"type":"Withdraw","amount":amount,"time":str(datetime.now())}
                )
                save_data(data)
                print("Withdraw successful.")

        elif choice == '4':
            print("\n*** Transaction History ***")
            for t in user["transactions"]:
                print(f"{t['time']}-{t['type']}:${t['amount']:.2f}")

        elif choice == '5':
            break
        else:
            print("Invalid option.")

def login(data):
    username=input("User name: ")
    password=input("Password: ")

    if username == data["admin"]["username"] and password == data["admin"]["password"]:
        while True:
            print("\n***Admin Menu***")
            print("1. Create Account")
            print("2. View All Accounts")
            print("3. Logout")
            
            choice = input("Choose an option: ")
            if choice == '1':
                create_account(data)
            elif choice == '2':
                view_all_accounts(data)
            elif choice == '3':
                break
            else:
                print("Invalid option")

    elif username in data["users"] and data["users"][username]["password"]==password:
        user_menu(username,data)
    else:
        print("Invalid login")

def main():
    data = load_data()
    while True:
        print("\n*****Bank App*****")
        print("1. Login")
        print("2. Exit")

        choice=input("choose an option: ")
        if choice == '1':
            login(data)
        elif choice =='2':
            print("Thankyou!")
            break
        else:
            print("invalid option.")

if __name__ == "__main__":
    main()

 




