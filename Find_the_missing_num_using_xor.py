numbers = list(map(int, input("Enter numbers: ").split()))

n = len(numbers) + 1
xor_all = 0
xor_numbers = 0

for i in range(1, n + 1):
    xor_all ^= i

for num in numbers:
    xor_numbers ^= num

missing = xor_all ^ xor_numbers

print("Missing number:", missing)
