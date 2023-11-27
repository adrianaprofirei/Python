import os
import sys

def ex4(directory_path):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError("Directory not found")

        if not os.path.isdir(directory_path):
            raise NotADirectoryError("Not a directory")

        files = os.listdir(directory_path)

        if not files:
            raise ValueError("Directory is empty")

        file_extension_counts = {}

        for file_name in files:
            if os.path.isfile(os.path.join(directory_path, file_name)):
                file_extension = os.path.splitext(file_name)[1]
                if file_extension:
                    file_extension = file_extension.lower()
                    if file_extension in file_extension_counts:
                        file_extension_counts[file_extension] += 1
                    else:
                        file_extension_counts[file_extension] = 1

        if not file_extension_counts:
            raise NotImplementedError("No files with extensions found.")
        else:
            print("Number of files by extension:")
            for extension, count in file_extension_counts.items():
                print(f"{extension}: {count}")

    except (FileNotFoundError, NotADirectoryError, ValueError, NotImplementedError) as e:
        print(f"Error: {e}")


directory_path = sys.argv[1]
ex4(directory_path)
