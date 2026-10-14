items = {}

while True:
    name = input("Item name (done to finish): ")

    if name.lower() == "done":
        break

    price = float(input("Price: "))
    items[name] = price

total = sum(items.values())

print("\n--- BILL ---")
for name, price in items.items():
    print(f"{name}: ₹{price:.2f}")

print(f"Total: ₹{total:.2f}")
