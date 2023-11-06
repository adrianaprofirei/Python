def ex1():
    class Stack:
        def __init__(self):
            self.__items = []

        def __iter__(self):
            raise TypeError("You cannot iterate there.")

        def __getitem__(self, item):
            raise TypeError("You cannot access the element.")

        def push(self, item):
            self.__items.append(item)

        def pop(self):
            if len(self.__items) == 0:
                return None
            else:
                return self.__items.pop()

        def peek(self):
            if len(self.__items) == 0:
                return None
            else:
                return self.__items[-1]

    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    # try:
    #     print(stack[0])
    # except TypeError as e:
    #     print(e)

    # print(stack._Stack__items[1])

    print(stack.peek())
    print(stack.pop())
    print()

    print(stack.peek())
    print(stack.pop())
    print()

    print(stack.peek())
    print(stack.pop())
    print()

    print(stack.peek())
    print(stack.pop())
    print()


print("Stack:")
ex1()


def ex2():
    class Queue:
        def __init__(self):
            self.__items = []

        def __iter__(self):
            raise TypeError("You cannot iterate there.")

        def __getitem__(self, item):
            raise TypeError("You cannot access the element.")

        def push(self, item):
            self.__items.append(item)

        def pop(self):
            if len(self.__items) == 0:
                return None
            else:
                return self.__items.pop(0)

        def peek(self):
            if len(self.__items) == 0:
                return None
            else:
                return self.__items[0]

    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)

    print(queue.peek())
    print(queue.pop())
    print()

    print(queue.peek())
    print(queue.pop())
    print()

    print(queue.peek())
    print(queue.pop())
    print()

    print(queue.peek())
    print(queue.pop())


print("Queue:")
ex2()


def ex3():
    class Matrix:
        def __init__(self, n, m):
            self.n = n
            self.m = m
            self.matrix = [[0] * m for _ in range(n)]

        def get(self, i, j):
            if 0 <= i < self.n and 0 <= j < self.m:
                return self.matrix[i][j]
            else:
                return "You are outside the matrix"

        def set(self, i, j, value):
            if 0 <= i < self.n and 0 <= j < self.m:
                self.matrix[i][j] = value
            else:
                return "You are outside the matrix"

        def transpose(self):
            transpose_matrix = Matrix(self.m, self.n)
            for i in range(self.n):
                for j in range(self.m):
                    transpose_matrix.set(j, i, self.get(i, j))
            return transpose_matrix

        def matrix_multiplication(self, mmatrix):
            if self.m != mmatrix.n:
                return "Multiplication cannot be done"
            result = Matrix(self.n, mmatrix.m)
            for i in range(self.n):
                for j in range(mmatrix.m):
                    product = 0
                    for k in range(self.m):
                        product += self.get(i, k) * mmatrix.get(k, j)
                    result.set(i, j, product)
            return result

        def apply_function(self, func):
            result = Matrix(self.n, self.m)
            for i in range(self.n):
                for j in range(self.m):
                    value = func(self.get(i, j))
                    result.set(i, j, value)
            return result

        def __str__(self):
            return "\n".join(["\t".join(map(str, row)) for row in self.matrix])

    matrix1 = Matrix(2, 3)
    matrix1.set(0, 0, 6)
    matrix1.set(0, 1, 5)
    matrix1.set(0, 2, 4)
    matrix1.set(1, 0, 3)
    matrix1.set(1, 1, 2)
    matrix1.set(1, 2, 1)

    print("First matrix:")
    print(matrix1)

    print("Transposed first matrix:")
    transpose_matrix1 = matrix1.transpose()
    print(matrix1)

    matrix2 = Matrix(3, 2)
    matrix2.set(0, 0, 7)
    matrix2.set(0, 1, 8)
    matrix2.set(1, 0, 9)
    matrix2.set(1, 1, 10)
    matrix2.set(2, 0, 11)
    matrix2.set(2, 1, 12)

    print("Second matrix:")
    print(matrix2)

    print("Multiply of the two matrix:")
    multiplied_matrix = matrix1.matrix_multiplication(matrix2)
    print(multiplied_matrix)

    print("All elements squared in first matrix:")
    applied_function = matrix1.apply_function(lambda x: x ** 2)
    print(applied_function)


ex3()