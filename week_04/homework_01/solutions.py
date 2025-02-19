from random import randint
from collections import defaultdict

def task_1() -> None:
    """
    Create an empty set called 'my_set'.
    """
    my_set = set()
    print(my_set)  # should print set()

def task_2() -> None:
    """
    Let's turn a given sentence into a set of words.
    """
    sentence = "abc cba acd abc"
    words = set(sentence.split())
    print(words)  # should be {'acd', 'cba', 'abc'} or in other order

def task_3() -> None:
    """
    Now, let's remove from `words` all the words that are present in `sentence2`.
    """
    sentence2 = 'cba baa acc'
    words = set("abc cba acd abc".split())
    words -= set(sentence2.split())
    print(words)  # should print {'acd', 'abc'} or {'abc', 'acd'}

def task_4() -> None:
    """
    Generate `N` random numbers in the range `[1, N]` and keep track of a percent of unique numbers in the result.
    """
    n = 10000000
    random_numbers = {randint(1, n) for _ in range(n)}
    percentage_unique = (len(random_numbers) / n) * 100
    print(f"Percentage of unique numbers: {percentage_unique:.2f}%")

def task_5() -> None:
    """
    You are given a matrix `m`. Return a distinct list containing all the values that are present in at least `n` rows.
    """
    m = [
        [1, 1, 2, 3],
        [1, 2, 6, 7],
        [1, 7, 9, 9]
    ]

    n = 2
    count_dict = defaultdict(int)
    for row in m:
        for num in set(row):  # Remove duplicates in a row
            count_dict[num] += 1

    res = [num for num, count in count_dict.items() if count >= n]
    print(res)  # should print [1, 2, 7]