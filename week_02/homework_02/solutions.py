def task_1() -> None:
    """
    Write a program that prints the numbers from `a` to `b` using a for loop.
    """
    a = 1
    b = 5

    for i in range(a, b + 1):
        print(i, end=" ")
    print()


def task_2() -> None:
    """
    Create a function called `is_prime` that takes a number as a parameter,
    returns `True` if the number is prime, and `False` otherwise.
    """

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    print("Is 11 a prime?", is_prime(11))  # should be True
    print("Is 9 a prime?", is_prime(9))  # should be False


def task_3() -> None:
    """
    Write a function called `find_primes` that takes two integers, `a` and `b`,
    and prints all the prime numbers between `a` and `b` (inclusive).
    """

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_primes(a: int, b: int) -> None:
        for i in range(a, b + 1):
            if is_prime(i):
                print(i, end=" ")
        print()

    find_primes(1, 11)  # should print 2 3 5 7 11


def task_4() -> None:
    """
    Write a function called `reverse_words` that takes a sentence as a parameter
    and prints the sentence with each word reversed, but the words remain in the same order.
    """

    def reverse_words(sentence: str) -> None:
        reversed_sentence = " ".join(word[::-1] for word in sentence.split())
        print(reversed_sentence)

    reverse_words("Quick brown fox jumps over a lazy dog")  # should print "kciuQ nworb xof spmuj revo a yzal god"
