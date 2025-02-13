def task_1():
    """
    Task 1: Modify the `calculate` function to ensure the program runs without errors.
    The function should track the number of times it is called.
    """
    call_counter = 0

    def calculate(a, b):
        nonlocal call_counter  # Дозволяє змінювати змінну у зовнішньому просторі
        call_counter += 1
        return a ** (b / 2)

    for _ in range(5):
        calculate(5, 5)

    print(f'calculate called {call_counter} times')  # повинно вивести "calculate called 5 times"


def task_2():
    """
    Task 2: Provide examples that raise specific errors (SyntaxError, ValueError, NameError).
    """
    # a: SyntaxError
    # print(hello world)  # Неправильний синтаксис

    # b: ValueError
    try:
        int("abc")  # Неможливо перетворити рядок на число
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    # c: NameError
    try:
        print(undefined_variable)  # Використання змінної, яка не визначена
    except NameError as e:
        print(f"Caught NameError: {e}")


def task_3():
    """
    Task 3: Given a tuple `a1`, create a new tuple `b1` that has all elements in reverse order.
    """
    a1 = (1, 2, 3, 4, 5)
    b1 = a1[::-1]  # Реверс кортежу
    print(b1)  # має вивести (5, 4, 3, 2, 1)


def task_4():
    """
    Task 4: Implement a function that removes an element from a tuple by index and returns a new tuple.
    """

    def pop_element(v1: tuple, i: int) -> tuple:
        return v1[:i] + v1[i + 1:]  # Створює новий кортеж без елемента на індексі i

    print(pop_element((1, 2, 3), 1))  # має вивести (1, 3)


def task_5():
    """
    Task 5: Implement a function to add vectors element-wise in the same-dimensional space.
    Raise ValueError if dimensions do not match.
    """

    def add(v1: tuple, v2: tuple) -> tuple:
        if len(v1) != len(v2):
            raise ValueError("Vectors must have the same dimension")
        return tuple(a + b for a, b in zip(v1, v2))

    print(add((1, 2, 3), (4, 5, 6)))  # має вивести (5, 7, 9)
    try:
        print(add((1, 2, 3), (4, 5, 6, 7)))  # має викликати помилку
    except ValueError as e:
        print(f"Caught ValueError: {e}")


def task_6():
    """
    Task 6: Implement a dot product function for two vectors.
    Raise ValueError if dimensions do not match.
    """

    def dot(v1: tuple, v2: tuple) -> int:
        if len(v1) != len(v2):
            raise ValueError("Vectors must have the same dimension")
        return sum(a * b for a, b in zip(v1, v2))

    print(dot((1, 2, 3), (4, 5, 6)))  # має вивести 32
    try:
        print(dot((1, 2, 3), (4, 5, 6, 7)))  # має викликати помилку
    except ValueError as e:
        print(f"Caught ValueError: {e}")