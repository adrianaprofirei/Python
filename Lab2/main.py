# Ex 1

# def fibonacci(n):
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     if n == 2:
#         return [0, 1]
#
#     fib = [0, 1]
#
#     while len(fib) < n:
#         current_fib = fib[-2] + fib[-1]
#         fib.append(current_fib)
#
#     return fib
#
# print(fibonacci(10))


# Ex 2

# import math
#
# def prim(n):
#     rad = float(n)
#     if n == 0 or n == 1:
#         return 0
#     elif n % 2 == 0 and n != 2:
#         return 0
#     for i in range(3, int(math.sqrt(rad)) + 1, 2):
#         if n % i == 0:
#             return 0
#     return 1
#
# def prime_list(numbers):
#     prime_numbers = []
#     for i in numbers:
#         if prim(i):
#             prime_numbers.append(i)
#     return prime_numbers
#
# numbers = [2, 5, 7, 11, 20, 30, 40, 50]
# print(prime_list(numbers))


# Ex 3

# def operations(a, b):
#     intersection = list(set(a) & set(b))
#     union = list(set(a) | set(b))
#     aminusb = list(set(a) - set(b))
#     bminusa = list(set(b) - set(a))
#
#     return intersection, union, aminusb, bminusa
#
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# res = operations(a, b)
# print("Intersection of A and B is: ", res[0])
# print("Union of A and B is: ", res[1])
# print("A minus B is: ", res[2])
# print("B minus A is: ", res[3])


# Ex 4

# def compose(notes, moves, pos):
#     song = []
#     n = len(notes)
#     pos = pos % n
#     song.append(notes[pos])
#
#     for i in moves:
#         pos = (pos + i) % n
#         song.append(notes[pos])
#
#     return song
#
# print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))


# Ex 5

# def replace_under_main_diagonal(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if i >= j:
#                 matrix[i][j] = 0
#     return matrix
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(replace_under_main_diagonal(matrix))


# Ex 6

# def search_in_list(x, *lists):
#     combined_lists = []
#     for sublist in lists:
#         combined_lists.extend(sublist)
#
#     counter = {}
#     for count in combined_lists:
#         counter[count] = counter.get(count, 0) + 1
#
#     result = []
#     for item, count in counter.items():
#         if count == x:
#             result.append(item)
#
#     return result
#
# list1 = [1,2,3]
# list2 = [2,3,4]
# list3 = [4,5,6]
# list4 = [4,1, "test"]
# x = 2
# print(search_in_list(x, list1, list2, list3, list4))


# Ex 7

# def palindrome(x):
#     int_to_string = str(x)
#     return int_to_string == int_to_string[::-1]
#
# def palindrome_tuple(list):
#     tuple = ()
#     count = 0
#     maxi = -1
#     for elem in list:
#         if palindrome(elem):
#             count = count + 1
#             if elem > maxi:
#                 maxi = elem
#     tuple = tuple + (count, maxi,)
#     return tuple
#
# list = [121, 132, 919, 500, 333]
# print(palindrome_tuple(list))


# Ex 8

# def ASCII(list, x=None, flag=None):
#     result = []
#
#     if x is None:
#         x = 1
#     if flag is None:
#         flag = True
#
#     for elem in list:
#         chars = []
#
#         for letter in elem:
#             ascii_code = ord(letter)
#             if flag and ascii_code % x == 0:
#                 chars.append(letter)
#             elif not flag and ascii_code % x != 0:
#                 chars.append(letter)
#         result.append(chars)
#
#     return result
#
#
# x = 2
# list = ["test", "hello", "lab002"]
# flag = False

# print(ASCII(list, x, flag))

# Ex 9
#
# def spectator_stadium(matrix):
#     n = len(matrix)
#     m = len(matrix[0])
#
#     res = []
#
#     for j in range(m):
#         highest = matrix[0][j]
#         for i in range(1, n):
#             if matrix[i][j] < highest:
#                 res.append((i, j))
#             highest = max(highest, matrix[i][j])
#
#     return res
#
# print(spectator_stadium(# FIELD
# [[1, 2, 3, 2, 1, 1],
#  [2, 4, 4, 3, 7, 2],
#  [5, 5, 2, 5, 6, 4],
#  [6, 6, 7, 6, 7, 5]] ))


# Ex 10

# def combine_in_tuple(*args):
#     max_length = max(len(arg) for arg in args)  # Find the maximum length among all input iterables
#     result = []
#
#     for i in range(max_length):
#         combined_elements = []
#         for arg in args:
#             if len(arg) > i:
#                 combined_elements.append(arg[i])
#             else:
#                 combined_elements.append(None)
#         combined_tuple = tuple(combined_elements)
#         result.append(combined_tuple)
#
#     return result
#
# print(combine_in_tuple([1,2,3], [5,6,7], ["a", "b", "c"]))


# Ex 11

# def order_tuple(list):
#     return sorted(list, key = lambda x: x[1][2])
#
# print(order_tuple([('abc', 'bcd'), ('abc', 'zza')]))


# Ex 12

# def group_by_rhyme(words):
#     res = {}
#
#     for word in words:
#         if word[-2:] in res:
#             res[word[-2:]].append(word)
#         else:
#             res[word[-2:]] = [word]
#
#     return list(res.values())
#
# print(group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']))
