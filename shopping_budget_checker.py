items = {
    "Laptop": 45000,
    "Headphones": 2000,
    "Mouse": 800
}

budget = 50000
total = sum(items.values())

print("Total Cost:", total)
print("Budget:", budget)

if total <= budget:
    print("Within Budget")
    print("Remaining:", budget - total)
else:
    print("Budget Exceeded")
    print("Extra Needed:", total - budget)
