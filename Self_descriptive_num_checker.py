num = input("Enter number: ")

valid = True

for digit in range(len(num)):
    if num.count(str(digit)) != int(num[digit]):
        valid = False
        break

if valid:
    print("Self-descriptive number")
else:
    print("Not self-descriptive")
