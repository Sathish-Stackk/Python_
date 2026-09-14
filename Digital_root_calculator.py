num = int(input("Enter number: "))

while num >= 10:
    total = 0
    while num:
        total += num % 10
        num //= 10
    num = total

print("Digital Root:", num)
