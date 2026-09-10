transactions = [
    ("Deposit", 5000),
    ("Withdraw", 1200),
    ("Withdraw", 800),
    ("Deposit", 2500),
    ("Withdraw", 600)
]

balance = 0
total_deposit = 0
total_withdraw = 0

for transaction, amount in transactions:

    if transaction == "Deposit":
        balance += amount
        total_deposit += amount

    elif transaction == "Withdraw":
        if amount <= balance:
            balance -= amount
            total_withdraw += amount
        else:
            print("Insufficient balance for:", amount)

print("\nTransaction Summary")
print("Total Deposited:", total_deposit)
print("Total Withdrawn:", total_withdraw)
print("Final Balance:", balance)
