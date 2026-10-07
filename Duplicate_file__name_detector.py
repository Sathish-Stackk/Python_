def find_duplicates(files):
    seen = set()
    duplicates = []

    for file in files:
        if file in seen and file not in duplicates:
            duplicates.append(file)
        else:
            seen.add(file)

    return duplicates


files = input("Enter file names separated by spaces: ").split()

duplicates = find_duplicates(files)

if duplicates:
    print("Duplicate files:")
    for file in duplicates:
        print("-", file)
else:
    print("No duplicate files found.")
