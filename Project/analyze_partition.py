import sys
import psutil
import os


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
