hours = float(input("Enter parking hours: "))

if hours <= 0:
    print("Invalid parking time")
elif hours <= 2:
    fee = 20
elif hours <= 5:
    fee = 20 + (hours - 2) * 10
else:
    fee = 50 + (hours - 5) * 15

print("Parking Fee: ₹", round(fee, 2))
