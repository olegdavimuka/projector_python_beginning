def task_1():
    """
    a. Write a program that prints the number 10.
    b. Declare another variable res2 with value 10. Print IDs of both.
    c. Declare two other variables with the value 10000. Print IDs of both
    """
    res1 = 10
    print(res1)

    res2 = 10
    print(id(res1), id(res2))

    var1 = 10000
    var2 = 10000
    print(id(var1), id(var2))


def task_2():
    """
    Now, write a program that gets a name from a user and prints "Hello, ".
    """
    name = input('Enter your name: ')  # what is input and why is it needed
    print(f'Hi, {name}')


def task_3():  # code should work for any two numbers
    """
    Write a program that gets two int variables and swaps their values. Do it in 3 different ways.
    """
    print('Option 1')
    a = 12731723
    b = 10

    temp = a
    a = b
    b = temp

    print('a =', a, 'b =', b)

    print('Option 2')
    a = 12731723
    b = 10

    a = a + b
    b = a - b
    a = a - b

    print('a =', a, 'b =', b)

    print('Option 3')
    a = 12731723
    b = 10

    a, b = b, a

    print('a =', int(a), 'b =', int(b))


def task_4():
    """
    Write a program that gets two numbers from the user. Print to the console the maximum of these two variables.
    """
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    res = max(a, b)

    print('res =', res)


def task_5():
    """
    You have two variables, x1 and x2. Complete the program that calculates the following function:
    x1 ** ((x2 - 1) / 2)
    """
    x1 = 10
    x2 = 5

    res = x1 ** ((x2 - 1) / 2)

    print('res =', res)  # should be 100.0


def task_6():
    """
    You have a variable x, always a two-digit number (e.g., 10 or 57). Complete the program that gets the last digit of
    this number (e.g., 10 -> 0, 57 -> 7).
    """
    x = 23127836817236

    res = x % 10

    print('res =', res)  # should be 7


if __name__ == '__main__':
    # task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    task_6()