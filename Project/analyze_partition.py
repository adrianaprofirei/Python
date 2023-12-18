import sys

import numpy
import psutil
import os
import matplotlib.pyplot as plt
import numpy as np


def get_partitions():
    partitions = psutil.disk_partitions()
    partition_list = [partition.device for partition in partitions]
    return partition_list


def is_valid_partition(partition_arg, partition_list):
    return partition_arg in partition_list


def list_directories(path):
    directory_count = 0
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            directory_count += 1
            print(os.path.join(root, dir))
    return directory_count


def list_files(path):
    file_count = 0
    for root, dirs, files, in os.walk(path):
        for file in files:
            file_count += 1
            print(os.path.join(root, file))
    return file_count


def get_files_extensions(path):
    extensions_list = {}
    extensions_size = {}
    for root, dirs, files, in os.walk(path):
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

def count_chart_pie(count_list, label_list):
    exts = np.array(count_list)
    labels = np.array(label_list)
    total = np.sum(exts)
    percentages = 100 * exts / total
    label_percentages = [f'{label}\n{percent:.3f}%' for label, percent in zip(labels, percentages)]
    patches, texts = plt.pie(exts, labels=label_percentages, radius=1.4)
    legend = plt.legend(patches, label_percentages, loc="center", ncol=11, title="Proportion of each file type "
                                                                                 "expressed in # of files with same "
                                                                                 "extension")
    plt.setp(legend.get_texts(), fontsize='small')  # Adjust 'large' as needed
    plt.show()


def size_chart_pie(count_list, label_list):
    exts = np.array(count_list)
    labels = np.array(size_list)
    total = np.sum(exts)
    percentages = 100 * exts / total
    label_percentages = [f'{label}\n{percent:.3f}%' for label, percent in zip(labels, percentages)]
    patches, texts = plt.pie(exts, labels=label_percentages, radius=1.4)
    legend = plt.legend(patches, label_percentages, loc="center", ncol=11, title="Proportion of each file type "
                                                                                 "expressed in size")
    plt.setp(legend.get_texts(), fontsize='small')  # Adjust 'large' as needed
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise Exception("Wrong number of parameters")
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
            print(f"Partition {path} does not contain any file.")
        else:
            print(f"Partition {path} has {file_count} files.")
        extensions_list, extensions_size = get_files_extensions(path)
        for ext, count in extensions_list.items():
            size = extensions_size.get(ext, 0)
            print(f"{ext}: {count} with {size} bytes")

        count_list = [count for ext, count in extensions_list.items()]
        label_list = [ext for ext, count in extensions_list.items()]
        size_list = []
        for ext, size in extensions_size.items():
            size_list.append(size)

        count_chart_pie(count_list, label_list)
        size_chart_pie(count_list, label_list)




