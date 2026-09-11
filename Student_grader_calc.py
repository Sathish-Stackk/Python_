marks = []

for i in range(5):
    mark = float(input(f"Enter subject {i + 1} marks: "))
    marks.append(mark)

average = sum(marks) / len(marks)

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Average:", round(average, 2))
print("Grade:", grade)
