isbn = input("Enter ISBN-10: ").replace("-", "")

if len(isbn) != 10:
    print("Invalid ISBN")
else:
    total = 0
    valid = True

    for i, char in enumerate(isbn):
        if char.isdigit():
            value = int(char)
        elif char.upper() == "X" and i == 9:
            value = 10
        else:
            valid = False
            break

        total += (10 - i) * value

    if valid and total % 11 == 0:
        print("Valid ISBN-10")
    else:
        print("Invalid ISBN-10")
