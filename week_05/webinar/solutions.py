from typing import Callable
import json
import time

def timing_decorator(func: Callable):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for {func.__name__}: {execution_time} seconds.")
        return result
    return wrapper

@timing_decorator
def add_two(a: int, b: int) -> int:
    return a + b

@timing_decorator
def add_three(a: int, b: int, c: int) -> int:
    return a + b + c

def task_1():
    """
    Create a decorator that can be applied to any function. This decorator should measure and print the time
    it takes for the decorated function to execute. Use the time module for measuring the execution time.
    """
    a, b, c = 5, 7, 10
    print(add_two(a, b))
    print(add_three(a, b, c))

def read_from_file(path: str) -> str:
    with open(path, "r") as file:
        return file.read()

def write_to_file_in_json_format(data: dict, path: str) -> None:
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

def count_words(text: str) -> dict[str, int]:
    words = text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def task_2():
    """
    Write a Python program that takes a filename as input and counts the number of
    occurrences for each word in the file. Write the word stats to a new file.
    """
    path_to_file = "your_path_to_txt_file"
    text = read_from_file(path_to_file)
    word_count = count_words(text)
    write_to_file_in_json_format(word_count, "your_path_to_json_file")

def sum_numbers(a: int, b: int, *args, **kwargs):
    sum_a_and_b = a + b
    sum_args = sum(args)
    sum_kwargs = sum(kwargs.values())
    return sum_a_and_b, sum_args, sum_kwargs

def task_3():
    print(sum_numbers(2, 3))
    print(sum_numbers(2, 3, 37))
    print(sum_numbers(2, 3, 78, 28))
    print(sum_numbers(2, 3, 78, 28, 2, 3, 78, 28, 2, 3, 78, 28, 2, 3, 78, 28))
    print(sum_numbers(2, 3, 78, 28, 2, 3, 78, 28, 2, 3, 78, 28, 2, 3, c=78, d=28))

    numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    numbers_dict = {"c": 1, "d": 2}
    print(sum_numbers(100, 200, *numbers_list, **numbers_dict))

if __name__ == "__main__":
    task_1()
    task_2()
    task_3()