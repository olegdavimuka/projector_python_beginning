def task_1() -> None:
    """
    Sum of Digits
    Write a program that takes an integer as input and calculates the sum of its digits.
    For example, if the input is 1234, the output should be 10.
    """
    number = input("Input your number: ")
    result = sum(int(digit) for digit in number)
    print(result)

def task_2() -> None:
    """
    Factorial
    Write a program that calculates the factorial of a given number.
    The factorial of a number n is the product of all positive integers less than or equal to n.
    For example, if the input is 5, the output should be 120 (since 5! = 5 * 4 * 3 * 2 * 1 = 120).
    """
    number = int(input("Input your number: "))
    result = 1
    for i in range(1, number + 1):
        result *= i
    print(result)

def task_3() -> None:
    """
    Prime Number Check
    Write a program that checks if a given number is prime. A prime number is a natural number greater than 1
    that has no positive divisors other than 1 and itself. For example, if the input is 7, the output should be true.
    """
    number = int(input("Input your number: "))
    if number < 2:
        result = False
    else:
        result = all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
    print(result)

def task_4() -> None:
    """
    Fibonacci Sequence
    Write a program that prints the Fibonacci sequence up to a given number of terms.
    The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones.
    For example, if the input is 8, the output should be 0, 1, 1, 2, 3, 5, 8, 13.
    """
    number = int(input("Input your number: "))
    fib_sequence = [0, 1]
    for _ in range(2, number):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    print(", ".join(map(str, fib_sequence[:number])))

task_1()
task_2()
task_3()
task_4()
