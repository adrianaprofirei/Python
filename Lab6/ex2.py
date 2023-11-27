import os
import sys

def ex2(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError("Directory not found")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError("Invalid directory path")

        files = os.listdir(directory_path)
        files.sort()

        if not files:
            raise ValueError("No files in the directory")

        for index, file_name in enumerate(files, start=1):
            old_file_path = os.path.join(directory_path, file_name)
            new_file_name = f"file{index}{os.path.splitext(file_name)[1]}"
            new_file_path = os.path.join(directory_path, new_file_name)

            try:
                os.rename(old_file_path, new_file_path)
                print(f"Renamed '{file_name}' to '{new_file_name}'")
            except OSError as e:
                print(f"Error renaming '{file_name}': {e}")

    except (FileNotFoundError, NotADirectoryError, ValueError) as e:
        print(f"Error: {e}")


directory_path = input()
ex2(directory_path)