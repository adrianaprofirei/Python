import sys
import psutil


def get_partitions():
    partitions = psutil.disk_partitions()
    partition_list = [partition.device for partition in partitions]
    return partition_list


def is_valid_partition(partition_arg, partition_list):
    return partition_arg in partition_list


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
