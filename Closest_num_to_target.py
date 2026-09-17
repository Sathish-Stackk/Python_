nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

closest = nums[0]

for n in nums:
    if abs(n - target) < abs(closest - target):
        closest = n

print("Target:", target)
print("Closest number:", closest)
print("Difference:", abs(closest - target))
