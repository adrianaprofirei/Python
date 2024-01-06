import sys
import pandas as pd
import psutil
import os
import plotly.express as px
import matplotlib.pyplot as plt


def get_partitions():
    partitions = psutil.disk_partitions()
    partition_list = [partition.device for partition in partitions]
    return partition_list


def is_valid_partition(partition, partition_list):
    return partition in partition_list


def list_directories(path):
    directory_count = 0
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir.startswith('$') or dir == 'System Volume Information':
                dirs.remove(dir)
            else:
                directory_count += 1
                print(os.path.join(root, dir))
    return directory_count


def list_files(path):
    file_count = 0
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if dir.startswith('$'):
                dirs.remove(dir)
        for file in files:
            file_count += 1
            print(os.path.join(root, file))
    return file_count


def get_files_extensions(path):
    extensions_list = {}
    extensions_size = {}
    for root, dirs, files, in os.walk(path):
        for dir in dirs[:]:
            if dir.startswith('$') or dir == 'System Volume Information':
                dirs.remove(dir)
        for file in files:
            try:
                extension = os.path.splitext(file)[1]
                if extension:
                    file_path = os.path.join(root, file)
                    file_size = os.path.getsize(file_path)
                    extensions_list[extension] = extensions_list.get(extension, 0) + 1
                    extensions_size[extension] = extensions_size.get(extension, 0) + file_size
            except (PermissionError, FileNotFoundError) as e:
                print(f"Error accessing file: {file}: {e}")
    return extensions_list, extensions_size


def convert_bytes(size_in_bytes):
    units = ["bytes", "KB", "MB", "GB", "TB"]
    unit_index = 0
    while size_in_bytes >= 1024 and unit_index < len(units) - 1:
        size_in_bytes /= 1024.0
        unit_index += 1
    return round(size_in_bytes, 2), units[unit_index]


def model_first_sunburst(data):
    data["extension"].append(ext)
    data["count"].append(count)
    data["size"].append(size)
    converted_size, unit = convert_bytes(size)
    data["converted_size"].append(f"{converted_size} {unit}")
    categories.append(ext)
    value.append(count)
    value_size.append(size)


def model_second_sunburst(data):
    data["extension"].append("Other")
    data["count"].append(other_count)
    data["size"].append(other_size)
    other_converted_size, other_unit = convert_bytes(other_size)
    data["converted_size"].append(f"{other_converted_size} {other_unit}")
    categories.append("Other")
    value.append(other_count)
    value_size.append(other_size)


def first_plot_bar(categories, value):
    plt.figure(figsize=(8, 6))
    plt.bar(categories, value, color='skyblue')
    plt.xlabel('Extension name')
    plt.ylabel('Count')
    plt.title('File count by extension')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def second_plot_bar(categories, value_size):
    plt.figure(figsize=(8, 6))
    plt.bar(categories, value_size, color='darkblue')
    plt.xlabel('Extension name')
    plt.ylabel('Count')
    plt.title('File sizes by extension')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


def sunburst_plot(data):
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=["extension"], values="count", title="File count by extension")
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    fig.show()
    fig = px.sunburst(df, path=["extension"], values="size", hover_data=["converted_size"],
                      title="File sizes by extension")
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    fig.show()


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise Exception("Wrong number of parameters; try using python analyze_partition.py <partition>")
        else:
            path = sys.argv[1]
            if len(path) == 1:
                path += ":\\"
            partition_list = get_partitions()
            if not is_valid_partition(path, partition_list):
                raise Exception("Specified partition does not exist.")

            directory_count = list_directories(path)
            file_count = list_files(path)

            if not directory_count:
                print(f"Partition {path} does not contain any directory.")
            else:
                print(f"Partition {path} has {directory_count} directories.")
            if not file_count:
                raise FileNotFoundError(f"partition {path} does not contain any files.")
            else:
                print(f"Partition {path} has {file_count} files.")

            extensions_list, extensions_size = get_files_extensions(path)

            total_count = 0
            total_size = 0

            for ext, count in extensions_list.items():
                size = extensions_size.get(ext, 0)
                total_count += count
                total_size += size
                print(f"{ext}: {count} with {size} bytes")

            data = {"extension": [], "count": [], "size": [], "converted_size": []}

            categories = []
            value = []
            value_size = []

            other_count = 0
            other_size = 0

            for ext, count in extensions_list.items():
                size = extensions_size.get(ext, 0)
                if count / total_count <= 0.0007 or size / total_size <= 0.0007:
                    other_count += count
                    other_size += size
                else:
                    model_first_sunburst(data)

            if other_count > 0 or other_size > 0:
                model_second_sunburst(data)

            sunburst_plot(data)
            first_plot_bar(categories, value)
            second_plot_bar(categories, value_size)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
