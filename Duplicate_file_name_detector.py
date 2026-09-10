files = [
    "resume.pdf",
    "project.py",
    "resume.pdf",
    "notes.txt",
    "project.py",
    "image.jpg"
]

seen = set()
duplicates = set()

for file in files:
    if file in seen:
        duplicates.add(file)
    else:
        seen.add(file)

print("Duplicate files:")

for file in duplicates:
    print(file)
