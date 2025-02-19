
# Team 1
def task_1():
    """
    O(1)
    Check if a number is even or odd.
    """
    def is_even(number: int) -> bool:
        return number % 2 == 0

    print(is_even(2))


def task_2():
    """
    O(n)
    Calculating n-th term of reccurence relation: f(n) = 3*f(n-1) + f(n-2)^2
    Hint: to obtain the complexity of O(n) you need to solve this using a list.
    """
    def nth_term(number: int) -> int:
        if number == 0:
            return 0
        if number == 1:
            return 1
        sequence = [0, 1]
        for i in range(2, number + 1):
            sequence.append(3 * sequence[i - 1] + sequence[i - 2] ** 2)
        return sequence[number]

    print(nth_term(5))

# Team 2
def task_3():
    """
    O(log n)
    Binary search in a sorted array.
    """
    def binary_search(numbers: list[int], target: int) -> int:
        left = 0
        right = len(numbers) - 1
        while left <= right:
            middle = (left + right) // 2
            if numbers[middle] == target:
                return middle
            elif numbers[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1

    print(binary_search([1, 2, 3, 4, 5], 3))


def task_4():
    """
    O(n)
    Checking if an array contains any duplicate elements.
    Hint: to obtain the complexity of O(n) you need to solve this using a set
    """
    def has_duplicates(numbers: list[int]) -> bool:
        seen = set()
        for number in numbers:
            if number in seen:
                return True
            seen.add(number)
        return False

    print(has_duplicates([1, 2, 3, 4, 5, 5]))

# Team 3
def task_5():
    """
    O(n^2)
    Checking if an array contains any duplicate elements.
    """
    def has_duplicates_slow(numbers: list[int]) -> bool:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] == numbers[j]:
                    return True
        return False

    print(has_duplicates_slow([1, 2, 3, 4, 5, 5]))


def task_6():
    """
    # O(2^n)
    # Calculating n-th term of reccurence relation: f(n) = 3*f(n-1) + f(n-2)^2
    """
    def nth_term_slow(number: int) -> int:
        if number == 0:
            return 0
        if number == 1:
            return 1
        return 3 * nth_term_slow(number - 1) + nth_term_slow(number - 2) ** 2

    print(nth_term_slow(5))

# Homework
def task_7():
    """
    Word Frequency Counter
    Given a text document, count the frequency of each word in the document.
    Example Input: "This is a sample text. This text is a good example."
    Example Output: {'This': 2, 'is': 2, 'a': 2, 'sample': 1, 'text': 2, 'good': 1, 'example': 1}
    """
    ...

def task_8():
    """
    Anagram Checker
    Given two strings, check if they are anagrams, i.e. contain the same number of each letter
    Example Input: "listen", "silent"
    Example Output: True
    """
    ...
