a = float(input("Enter side 1: "))
b = float(input("Enter side 2: "))
c = float(input("Enter side 3: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print("Valid Equilateral Triangle")
        elif a == b or b == c or a == c:
            print("Valid Isosceles Triangle")
        else:
            print("Valid Scalene Triangle")
    else:
        print("Invalid Triangle")
else:
    print("Sides must be positive")
