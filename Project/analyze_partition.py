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
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            print(os.path.join(root, dir))


def list_files(path):
    for root, dirs, files, in os.walk(path):
        for file in files:
            print(os.path.join(root, file))


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
        # list_directories(path)
        list_files(path)
