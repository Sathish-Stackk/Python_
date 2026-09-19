n = int(input("Enter a number: "))

while n >= 10:
    total = 0
    while n:
        total += n % 10
        n //= 10
    n = total

print("Digital root:", n)
