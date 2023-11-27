import os
import sys


def calculate_total_size(directory_path):
    total_size = 0
    file_count = 0

    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError("Directory does not exist.")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError("Invalid directory path")

        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    file_size = os.path.getsize(file_path)
                    total_size += file_size
                    file_count += 1
                except OSError as e:
                    print(f"Error accessing file '{file_path}': {e}")

        if file_count == 0:
            print(f"No files found in '{directory_path}'")
        else:
            print(f"Total size of all {file_count} files in '{directory_path}': {total_size} bytes")

    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")


directory_path = sys.argv[1]
calculate_total_size(directory_path)
