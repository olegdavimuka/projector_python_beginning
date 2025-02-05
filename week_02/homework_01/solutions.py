from typing import Any


def task_1() -> None:
    """
    Implement a logical expression that turns the res on only when either switch1 or switch2 is on, but not both.
    """
    switch1 = True
    switch2 = False

    result = switch1 != switch2

    print(result)  # should be True


def task_2() -> None:
    """
    Declare variable a with some number.
    If the number is divisible by 5, print 'Yes', otherwise print 'No'.
    """
    a = 10

    if a % 5 == 0:
        print("Yes")
    else:
        print("No")


def task_3() -> None:
    """
    If the string a is empty, assign 'empty' to it.
    Otherwise, repeat the string five times.
    """
    a = "hello"

    result = "empty" if not a else a * 5

    print(result)


def task_4() -> None:
    """
    Calculate the sum of the first n terms of the harmonic series.
    """
    n = 10
    result = 0.0

    i = 1
    while i <= n:
        result += 1 / i
        i += 1

    print(result)  # should be 2.928968...


def task_5() -> None:
    """
    Calculate the sum of the first n terms of the alternating harmonic series.
    """
    n = 10
    result = 0

    for i in range(1, n + 1):
        result += (-1) ** (i + 1) / i

    print(result)  # should be 0.6456349...


def task_6() -> None:
    """
    Print the reverse of a given string using a while loop.
    """
    string = "some_string"
    reverse = ""

    index = len(string) - 1
    while index >= 0:
        reverse += string[index]
        index -= 1

    print(reverse)  # should be "gnirts_emos"


def task_7() -> None:
    """
    Identify and classify the shape using a match statement.
    """
    shape = "triangle"

    match shape:
        case "square":
            print("This is a square.")
        case "circle":
            print("This is a circle.")
        case "triangle":
            print("This is a triangle.")
        case _:
            print("Unknown shape.")


def task_8() -> None:
    """
    Function that processes different data types using a match statement.
    """

    def process_data(data: Any) -> str:
        match data:
            case int(data_int):
                return f"Processing number: {data_int * 2}"
            case float(data_float):
                return f"Processing float: {data_float / 2}"
            case str(data_str):
                return f"Processing string: {data_str.upper()}"
            case bool(data_bool):
                return f"Processing boolean: {not data_bool}"
            case _:
                return "Unsupported data type"

    print(process_data(11))
    print(process_data(3.14))
    print(process_data("hello"))
    print(process_data(True))


def task_9() -> None:
    """
    Function that processes different options using a match statement.
    """

    def process_options(option: str) -> None:
        match option:
            case "A" | "a":
                print("Option A selected.")
            case "B" | "b":
                print("Option B selected.")
            case "C" | "c":
                print("Option C selected.")
            case _:
                print("Invalid input")

    process_options("A")
    process_options("b")
    process_options("X")  # should print "Invalid input"
