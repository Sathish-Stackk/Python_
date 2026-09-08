import os
import shutil

folder = input("Enter folder path: ")

file_types = {
    ".jpg": "Images",
    ".png": "Images",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".docx": "Documents",
    ".mp3": "Music",
    ".mp4": "Videos"
}

for file in os.listdir(folder):

    path = os.path.join(folder, file)

    if os.path.isfile(path):
        extension = os.path.splitext(file)[1].lower()

        if extension in file_types:
            folder_name = file_types[extension]
            destination = os.path.join(folder, folder_name)

            os.makedirs(destination, exist_ok=True)

            shutil.move(
                path,
                os.path.join(destination, file)
            )

            print(file, "->", folder_name)

print("Files organized successfully.")
