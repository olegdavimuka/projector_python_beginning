def task_1() -> None:
    """
    Find a maximum element in a sorted list `li`. You can assume `li` to be non-empty.
    Complexity: O(1)
    """

    def find_max(li: list[int]) -> int:
        return li[-1]

    print(find_max([1, 2, 3, 4, 5]))  # should print 5
    print("O(1)")


def task_2() -> None:
    """
    Find a maximum element in an unsorted list `li`. You can assume `li` to be non-empty.
    Complexity: O(n)
    """

    def find_max(li: list[int]) -> int:
        max_val = li[0]
        for num in li:
            if num > max_val:
                max_val = num
        return max_val

    print(find_max([3, 1, 4, 1, 5, 9, 2, 6]))  # should print 9
    print("O(n)")


def task_3() -> None:
    """
    Implement a number guessing game where the program makes guesses and the user provides feedback.
    Complexity: O(log n)
    """
    n = 100
    a, b = 1, n
    while True:
        guess = (a + b) // 2
        print(f"Is it {guess}? (<, >, bingo)")
        response = input().strip()
        if response == "bingo":
            break
        elif response == "<":
            b = guess - 1
        elif response == ">":
            a = guess + 1
    print("O(log n)")