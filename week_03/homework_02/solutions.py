def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def task_1():
    """
    Let's recall the function find_primes from the previous assignment. Now, instead of printing the primes,
    let's append them to a list and return this list. Use for-loop for that.
    """
    def find_primes(a, b):
        primes = []
        for num in range(a, b + 1):
            if is_prime(num):
                primes.append(num)
        return primes

    print(find_primes(1, 11))  # should print [2, 3, 5, 7, 11]


def task_2():
    """
    Everything's the same as in the previous task, but now use list comprehension instead of the for-loop.
    """
    def find_primes(a, b):
        return [num for num in range(a, b + 1) if is_prime(num)]

    print(find_primes(1, 11))  # should print [2, 3, 5, 7, 11]


def task_3():
    """
    Complete the slicing operator so that the resulting list contains only numbers on the odd indices of the original list.
    """
    list_in = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_out = list_in[1::2]  # Slicing with step of 2, starting from index 1
    print(list_out)  # should print [1, 3, 5, 7, 9]


def task_4():
    """
    Sort the list unsorted_list in the following order: even numbers should go first, followed by odd numbers.
    """
    def is_even(num):
        return num % 2 == 0

    unsorted_list = [1, 2, 3, 4, 5, 6, 7]
    unsorted_list.sort(key=is_even)  # Sort by the result of is_even function
    print(unsorted_list)  # should print [2, 4, 6, 1, 3, 5, 7]


def task_5():
    """
    You are given a terrain map where 0 means water and 1 means land.
    Print the map to the console using a whitespace ' ' for water and 'X' for land.
    Please also add a border with '-' for lines and '+' for corners.
    """
    terrain_map = [
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 1, 1, 1],
        [1, 1, 1, 1]
    ]

    width = len(terrain_map[0])
    print("+" + "-" * width + "+")
    for row in terrain_map:
        print("|" + "".join("X" if cell else " " for cell in row) + "|")
    print("+" + "-" * width + "+")
