students = {
    "Sathish": 82,
    "Rahul": 91,
    "Kiran": 76,
    "Anil": 88,
    "Vamsi": 95
}

ranking = sorted(
    students.items(),
    key=lambda student: student[1],
    reverse=True
)

print("Student Rankings")

for rank, (name, marks) in enumerate(ranking, start=1):
    print(f"{rank}. {name} - {marks}")
