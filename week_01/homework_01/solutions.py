def task_1() -> None:
    """
    a. Write a program that prints the number 10.
    b. Declare another variable res2 with value 10. Print IDs of both.
    c. Declare two other variables with the value 10000. Print IDs of both.
    """
    res1 = 10
    print(res1)

    res2 = 10
    print(id(res1), id(res2))

    var1 = 10000
    var2 = 10000
    print(id(var1), id(var2))


def task_2() -> None:
    """
    Write a program that gets a name from a user and prints "Hello, <name>".
    """
    name = input("Enter your name: ")
    print(f"Hello, {name}")


def task_3() -> None:
    """
    Write a program that gets two int variables and swaps their values. Do it in 3 different ways.
    """
    print("Option 1")
    a, b = 3, 5

    # Using a temporary variable
    temp = a
    a = b
    b = temp
    print("a =", a, "b =", b)

    print("Option 2")
    a, b = 3, 5

    # Using arithmetic operations
    a = a + b
    b = a - b
    a = a - b
    print("a =", a, "b =", b)

    print("Option 3")
    a, b = 3, 5

    # Using tuple unpacking
    a, b = b, a
    print("a =", a, "b =", b)


def task_4() -> None:
    """
    Write a program that gets two numbers from the user. Print to the console the maximum of these two variables.
    """

    def get_valid_int(prompt: str) -> int:
        """
        Helper function to get a valid integer from the user.
        """
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    a = get_valid_int("Enter the first number: ")
    b = get_valid_int("Enter the second number: ")

    result = max(a, b)
    print(result)


def task_5() -> None:
    """
    You have two variables, x1 and x2. Complete the program that calculates the following function:
    x1 ** ((x2 - 1) / 2)
    """
    x1 = 10
    x2 = 5

    result = x1 ** ((x2 - 1) / 2)
    print(result)  # should be 100.0


def task_6() -> None:
    """
    You have a variable x, always a two-digit number (e.g., 10 or 57). Complete the program that gets the last digit of
    this number (e.g., 10 -> 0, 57 -> 7).
    """
    x = 57

    result = x % 10
    print(result)  # should be 7
