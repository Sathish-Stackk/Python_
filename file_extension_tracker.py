files = input("Enter filenames: ").split()

extensions = {}

for file in files:
    if "." in file:
        ext = file.split(".")[-1].lower()
        extensions[ext] = extensions.get(ext, 0) + 1

print("\nFile Summary")
for ext, count in extensions.items():
    print(f".{ext}: {count} file(s)")
