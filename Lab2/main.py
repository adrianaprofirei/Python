# Ex 1
#Write a function to return a list of the first n numbers in the Fibonacci string.

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
#Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

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
#Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)

# def operations(a, b):
#     intersection = []
#     for elem in a:
#         if elem in b:
#             intersection.append(elem)
#     union = a[:]
#     for elem in b:
#         if elem not in union:
#             union.append(elem)
#     aminusb = []
#     for elem in a:
#         if elem not in b:
#             aminusb.append(elem)
#     bminusa = []
#     for elem in b:
#         if elem not in a:
#             bminusa.append(elem)
#
#     return intersection, union, aminusb, bminusa
#
# a = [2, 3, 6, 3]
# b = [7, 4, 2, 8, 6, 2]
# res = operations(a, b)
# print("Intersection of A and B is: ", res[0])
# print("Union of A and B is: ", res[1])
# print("A minus B is: ", res[2])
# print("B minus A is: ", res[3])


# Ex 4
#Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer). The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter. Example :
# compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2)
# will return ["mi", "fa", "do", "sol", "re"]

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
#Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).

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
#Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists. Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1 and 2, 3 is in lists 1 and 2.

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
#Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. The first element of the tuple will be the number of palindrome numbers

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
#Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x. Example:
# x = 2, ["test", "hello", "lab002"], flag = False
# will return (["e", "s"], ["e","o"], ["a"]) . Note: The function must return list of lists.

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
#Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field. Example:
# FIELD
# [[1, 2, 3, 2, 1, 1],
#  [2, 4, 4, 3, 7, 2],
#  [5, 5, 2, 5, 6, 4],
#  [6, 6, 7, 6, 7, 5]]
# Will return : [(2, 2), (3, 4), (2, 4)]

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
#Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc. Example: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to generate max ([len(x) for x in input_lists]) tuples.

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
#Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. Example:
# ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

# def order_tuple(list):
#     return sorted(list, key = lambda x: x[1][2])
#
# print(order_tuple([('abc', 'bcd'), ('abc', 'zza')]))


# Ex 12
#Write a function that will receive a list of words as parameter and will return a list of lists of words, grouped by rhyme. Two words rhyme if both of them end with the same 2 letters. Example: group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']]

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
