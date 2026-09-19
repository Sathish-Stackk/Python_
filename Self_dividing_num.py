n = int(input("Enter a number: "))
original = n
valid = True

while n:
    digit = n % 10
    if digit == 0 or original % digit != 0:
        valid = False
        break
    n //= 10

print("Self-dividing" if valid else "Not self-dividing")
