numbers = list(map(int, input("Enter numbers: ").split()))

n = len(numbers) + 1
expected = n * (n + 1) // 2
actual = sum(numbers)

print("Missing Number:", expected - actual)
