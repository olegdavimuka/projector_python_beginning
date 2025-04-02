# TDD - Test Driven Development

# 1. Write a test
# 2. Run the test and see it fail
# 3. Write the code to make the test pass


def test_calculator():
    assert calculator(2, 3, '+') == 5
    assert calculator(5, 2, '-') == 3
    assert calculator(2, 3, '*') == 6
    assert calculator(6, 2, '/') == 3
    assert calculator(5, 0, '/') == "Cannot divide by zero"
    assert calculator(5, 2, '%') == "Invalid operator"


def calculator(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"
