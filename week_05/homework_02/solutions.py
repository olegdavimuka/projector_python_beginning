from typing import List, Callable
from datetime import datetime


def task_1() -> None:
    """
    Apply a function to each element of the list.
    """

    def apply(li: List[int], func: Callable[[int], int]) -> List[int]:
        return [func(num) for num in li]

    a = [1, 2, 3]

    def times_2(num: int) -> int:
        return num * 2

    print(apply(a, times_2))  # should print [2, 4, 6]


def task_2() -> None:
    """
    Apply a lambda function to a list.
    """
    def apply(li: List[int], func: Callable[[int], int]) -> List[int]:
        return [func(num) for num in li]

    b = [4, 5, 6]
    print(apply(b, lambda x: x * 2))  # should print [8, 10, 12]

def task_3() -> None:
    """
    Return the sum of even numbers from a list.
    """

    def sum_even(li: List[int]) -> int:
        def is_even(num: int) -> bool:
            return num % 2 == 0

        return sum(num for num in li if is_even(num))

    print(sum_even([1, 2, 3, 4, 5, 6]))  # should print 12


def task_4() -> None:
    """
    Decorator that logs function calls.
    """

    def add_logging(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            print(f"function `{func.__name__}` called at {datetime.now().isoformat()}Z")
            return func(*args, **kwargs)

        return wrapper


def task_5() -> None:
    """
    Apply `@add_logging` decorator to a function.
    """

    def add_logging(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            print(f"function `{func.__name__}` called at {datetime.now().isoformat()}Z")
            return func(*args, **kwargs)

        return wrapper

    @add_logging
    def some_function():
        print("Executing some_function")

    some_function()  # should print log message and "Executing some_function"