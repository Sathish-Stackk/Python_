balance = float(input("Enter account balance: "))
amount = float(input("Enter withdrawal amount: "))

if amount <= 0:
    print("Invalid withdrawal amount")
elif amount > balance:
    print("Insufficient balance")
elif amount % 100 != 0:
    print("Amount must be a multiple of 100")
elif balance - amount < 500:
    print("Minimum balance of ₹500 must be maintained")
else:
    balance -= amount
    print("Withdrawal successful")
    print("Remaining balance: ₹", balance)
