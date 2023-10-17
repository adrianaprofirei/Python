#Ex 1
#Find The greatest common divisor of multiple numbers read from the console.

# def gcd(a, b):
#     while b:
#         a, b = b, a%b
#     return a
#
# def gcd_multiple_numbers():
#     res = int(input())
#     if res == 0:
#         return 0
#     y = int(input())
#     if y == 0:
#         return res
#     res = gcd(res, y)
#     while True:
#         x = int(input())
#         if x == 0:
#             break
#         res = gcd(res, x)
#     return res
#
# result = gcd_multiple_numbers()
# print("The greatest common divisor of the numbers above is ", result)


#Ex 2
#Write a script that calculates how many vowels are in a string.

# def vowel_number(string):
#     vowels = 'aeiouAEIOU'
#     count = 0
#     for i in string:
#         if i in vowels:
#             count += 1
#     return count
#
# print(vowel_number("Astazi este 16 octombrie"))


#Ex 3
#Write a script that receives two strings and prints the number of occurrences of the first string in the second.

# def occurencies_number(string1, string2):
#     count = 0
#     for i in range(len(string2) - len(string1) + 1):
#         if string2[i:i + len(string1)] == string1:
#             count += 1
#     return count
# 
# print(occurencies_number("AA", "AAAA"))


#Ex 4
#Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

# def camel_to_lower(string):
#     new = ""
#     for char in string:
#         if char.isupper():
#             new = new + "_" + char.lower()
#         else:
#             new = new + char
#     return new
#
# print(camel_to_lower("Salut, Calin! Ce faci in Bucuresti? OK!"))


#Ex 5
#Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in t
he example):
firs      1  2  3  4    =>   first_python_lab
n_lt      12 13 14 5
oba_      11 16 15 6
htyp      10 9  8  7

# def spiralmatrix(matrix):
#     new = []
#     while matrix:
#         #top
#         new.extend(matrix[0])
#         matrix.pop(0)
#         #right
#         if matrix:
#             for row in matrix:
#                 new.append(row[-1])
#                 row.pop()
#         #bottom
#         if matrix:
#             new.extend(matrix[-1][::-1])
#             matrix.pop(-1)
#         #left
#         if matrix:
#             for row in matrix[::-1]:
#                 new.append(row[0])
#                 row.pop(0)
#         print("4", matrix)
#
#
#     return ''.join(new)
#
# matrix = [
#         ["f", "i", "r", "s"],
#         ["n", "_", "l", "t"],
#         ["o", "b", "a", "_"],
#         ["h", "t", "y", "p"]
#     ]
# print(spiralmatrix(matrix))


#Ex 6
#Write a function that validates if a number is a palindrome.

# def palindrome(x):
#     int_to_string = str(x)
#     return int_to_string == int_to_string[::-1]
#
# print(palindrome("capac"))


#Ex 7
#Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.

# def extract_number(string):
#     new = ""
#     ok = 0
#     for i in range(len(string)):
#         if string[i].isdigit():
#             new += string[i]
#             ok = 1
#         else:
#             if ok:
#                 break  # Stop once a sequence of digits ends
#     return new
#
# print(extract_number("abc123abc"))


#Ex 8
#Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"

# def bit_number(x):
#     count = 0
#     bit_string = format(x, 'b')
#     for i in range(len(bit_string)):
#         if(bit_string[i] == "1"):
#             count += 1
#     return count
#
# print(bit_number(24))


#Ex 9
#Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.

# def most_common_letter(string):
#     freq = [0] * 26
#     string = string.lower()
#
#     for char in string:
#         if char.isalpha():
#             index = ord(char) - ord('a')
#             freq[index] += 1
#     max_count = max(freq)
#     most_common = chr(freq.index(max_count) + ord('a'))
#     return most_common
#
# result = most_common_letter("abcda")
# print(most_common_letter("an apple is not a tomato"))


#Ex 10
#Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 words.

# def word_number(string):
#     count = 1
#     for i in string:
#         if i == " ":
#             count += 1
#     return count
#
# print(word_number("I have Python exam"))
