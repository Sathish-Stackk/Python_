nums = list(map(int, input("Enter numbers: ").split()))

positive = [x for x in nums if x >= 0]
negative = [x for x in nums if x < 0]

result = []
while positive or negative:
    if positive:
        result.append(positive.pop(0))
    if negative:
        result.append(negative.pop(0))

print("Rearranged:", result)
