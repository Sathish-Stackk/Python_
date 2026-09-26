marks = [85, 72, 91, 68, 79]

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("Marks:", marks)
print("Average:", round(average, 2))
print("Highest:", highest)
print("Lowest:", lowest)

print("Result:", "Pass" if average >= 40 else "Fail")
