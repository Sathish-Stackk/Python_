numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotation value: "))

k = k % len(numbers)

rotated = numbers[-k:] + numbers[:-k]

print("Rotated list:", rotated)
