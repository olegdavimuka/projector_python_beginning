def task_1() -> None:
    """
    Replace all TODOs with one of the logical operators to make all the expressions True.
    """
    print("1", 4 < 5)
    print("2", 10 > 5)
    print("3", 42 == 42)
    print("4", 42 != "42")
    print("5", "None" != None)  # noqa


def task_2() -> None:
    """
    You have a string in the variable a. Remove all letters e from it.
    """
    a = "Somebody said something to Samantha."

    result = a.replace("e", "")

    print(result)  # Should be "Sombody said somthing to Samantha"


def task_3() -> None:
    """
    Make all letters of the string a lowercase.
    """
    a = "Animals"

    result = a.lower()

    print(result)  # Should be "animals"


def task_4() -> None:
    """
    Remove all spaces from the beginning and end of the string a.
    """
    a = "   Fancy string   "

    result = a.strip()

    print(result)  # Should be "Fancy string"


def task_5() -> None:
    """
    Remove all spaces from the end of the string a.
    """
    a = "   Fancy string   "

    result = a.rstrip()

    print(result)  # Should be "   Fancy string"
