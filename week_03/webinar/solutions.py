def task_1() -> None:
    """
    Intersection and merge of two sorted lists
    a. Write a function that returns an intersection of two sorted lists of integers in non-decreasing order.
    b. Write a function that returns a merge of two sorted lists of integers  in non-decreasing order.
    """

    def intersection(a: list, b: list) -> list:
        i, j = 0, 0
        result = []

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else:
                result.append(a[i])
                i += 1
                j += 1

        return result

    def merge(a: list, b: list) -> list:
        i, j = 0, 0
        result = []

        while i != len(a) and j != len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        result.extend(a[i:])
        result.extend(b[j:])

        return result

    a = [1, 2, 3]
    b = [2, 3, 4, 5, 6]

    print(intersection(a, b) == [2, 3])
    print(merge(a, b) == [1, 2, 2, 3, 3, 4, 5, 6])


def task_2() -> None:
    """
    Move zeroes
    Given an integer array numbers, move all 0's to the end of it while maintaining the relative order of the non-zero
    elements.
    """

    def move_zeroes(numbers: list) -> list:
        non_zero_index = 0

        # Move all non-zero elements to the front of the list
        for i in range(len(numbers)):
            if numbers[i] != 0:
                numbers[non_zero_index], numbers[i] = numbers[i], numbers[non_zero_index]
                non_zero_index += 1

        return numbers

    numbers = [0, 1, 0, 3, 12]
    print(move_zeroes(numbers) == [1, 3, 12, 0, 0])


def task_3() -> None:
    """
    Shuffle list
    Given a list, shuffle it so that the elements from the second half appear between the elements from the first half.
    """

    def shuffle_list(numbers : list) -> list:
        mid = len(numbers) // 2
        shuffled = []

        for i in range(mid):
            shuffled.append(numbers[i])
            if mid + i < len(numbers):
                shuffled.append(numbers[mid + i])

        return shuffled

    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    print(shuffle_list(numbers) == [1, 5, 2, 6, 3, 7, 4, 8])

def task_4() -> None:
    """
    Greatest common divisor of list
    Given a list, find the greatest common divisor of all the elements in the list.
    """

    def gcd(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    def gcd_list(numbers: list) -> int:
        current_gcd = numbers[0]

        for num in numbers[1:]:
            current_gcd = gcd(current_gcd, num)

            # Early exit if GCD becomes 1
            if current_gcd == 1:
                return 1

        return current_gcd

    numbers = [16, 32, 4]

    print(gcd_list(numbers) == 4)
