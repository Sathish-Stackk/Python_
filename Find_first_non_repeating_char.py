text = input("Enter a string: ")

found = False

for char in text:
    if text.count(char) == 1:
        print("First non-repeating character:", char)
        found = True
        break

if not found:
    print("No non-repeating character found")
