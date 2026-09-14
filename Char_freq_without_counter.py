text = input("Enter text: ").lower()
frequency = {}

for char in text:
    if char.isalpha():
        frequency[char] = frequency.get(char, 0) + 1

for char, count in sorted(frequency.items()):
    print(char, ":", count)
