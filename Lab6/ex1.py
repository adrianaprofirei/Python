import os
import sys


def ex1(directory_path, file_extension):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError("Directory not found")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError("Invalid directory path")

        if not file_extension.startswith("."):
            raise ValueError("Invalid extension")

        files_found = False

        for file_name in os.listdir(directory_path):
            if file_name.endswith(file_extension):
                files_found = True
                file_path = os.path.join(directory_path, file_name)
                try:
                    with open(file_path, 'r') as file:
                        contents = file.read()
                        print(f"Contents of {file_name}:")
                        print(contents)
                except IOError as e:
                    print(f"Error reading {file_name}: {e}")

        if not files_found:
            raise ValueError(f"No files with the extension '{file_extension}' found in the directory.")

    except (FileNotFoundError, NotADirectoryError, ValueError) as e:
        print(f"Error: {e}")


directory_path = sys.argv[1]
file_extension = sys.argv[2]
ex1(directory_path, file_extension)
