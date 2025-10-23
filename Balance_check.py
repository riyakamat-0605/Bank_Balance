initial_balance = float(input("Enter initial balance: ₹"))
deposit = float(input("Enter deposit amount: ₹"))

balance = initial_balance + deposit
print(f"Initial Balance: ₹{initial_balance}")
print(f"Deposit: ₹{deposit}")
print(f"New Balance after deposit: ₹{balance}")

withdraw = float(input("Enter amount to withdraw: ₹"))

if withdraw > balance:
    print("Insufficient balance!")
else:
    balance -= withdraw
    print(f"Withdraw: ₹{withdraw}")
    print(f"Final Balance: ₹{balance}")
