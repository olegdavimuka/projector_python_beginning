def task_1():
    """
    Replace all TODOs with one of the logical operators to make all the expressions True.
    """
    print('1', 4 < 5)
    print('2', 10 > 5)
    print('3', 42 == 42)
    print('4', 42 != "42")
    print('5', 'None' != None)

def task_2():
    """
    You have a string in the variable a. Remove all letters e from it.
    """
    a = "Somebody said something to Samantha."

    res = a.replace("e", "")

    print('res =', res)  # Should be "Sombody said somthing to Samantha"

def task_3():
    """
    Make all letters of the string a lowercase.
    """
    a = 'Animals'

    res = a.lower()

    print('res =', res)  # Should be "animals"


def task_4():
    """
    Remove all spaces from the beginning and end of the string a.
    """
    a = '   Fancy string   '

    res = a.strip()

    print('res =', res)  # Should be "Fancy string"


def task_5():
    """
    Remove all spaces from the  end of the string a.
    """
    a = '   Fancy string   '

    res = a.rstrip()

    print('res =', res)  # Should be "   Fancy string"

if __name__ == '__main__':
    task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()