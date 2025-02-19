import timeit

# O(n)
def nth_term(number: int) -> int:
    if number == 0:
        return 0
    if number == 1:
        return 1
    sequence = [0, 1]
    for i in range(2, number + 1):
        sequence.append(3 * sequence[i - 1] + sequence[i - 2] ** 2)
    return sequence[number]

# O(2^n)
def nth_term_reccursion(number: int) -> int:
    if number == 0:
        return 0
    if number == 1:
        return 1
    return 3 * nth_term_reccursion(number - 1) + nth_term_reccursion(number - 2) ** 2

# O(n)
def has_duplicates(numbers: list[int]) -> bool:
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False

# O(n^2)
def has_duplicates_slow(numbers: list[int]) -> bool:
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j]:
                return True
    return False


if __name__ == "__main__":
    print("Time taken by nth_term:", timeit.timeit(lambda: nth_term(10), number=1000))
    print("Time taken by nth_term_reccursion:", timeit.timeit(lambda: nth_term_reccursion(10), number=1000))

    list_to_check = [x for x in range(10)]
    print("Time taken by has_duplicates:", timeit.timeit(lambda: has_duplicates(list_to_check), number=1000))
    print("Time taken by has_duplicates_slow:", timeit.timeit(lambda: has_duplicates_slow(list_to_check), number=1000))