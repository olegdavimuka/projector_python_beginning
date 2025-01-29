def task_1():
    """
    Convert a snake_case string to a camelCase string
    """

    input_str = "this_is_snake_case"

    words = input_str.split("_")  # ['this', 'is', 'snake', 'case']
    # result = words[0] + ''.join([word.capitalize() for word in words[1:]])
    result = words[0]
    for word in words[1:]:
        result += word.capitalize()

    expected = "thisIsSnakeCase"
    print("camelCase string: ", result)
    print(result == expected)  # should be True


def task_2():
    """
    Count the number of words in a string
    """

    sentence = "This is sample sentence with spaces."

    word_count = len(sentence.split(" "))

    expected = 7
    print("Number of words:", word_count)
    print(word_count == expected)  # should be True


def task_3():
    """
    Replace Multiple Spaces with a Single Space
    """

    sentence = "This   is a    sample   sentence with spaces."

    words = sentence.split()
    result = " ".join(words)

    expected = "This is a sample sentence with spaces."
    print("Sentence with single spaces: ", result)
    print(result == expected)  # should be True


def is_palindrome(word):
    word_reversed = word[::-1]
    return word.lower() == word_reversed.lower()


def task_4():
    """
    Check if the string is a palindrome
    """

    word1 = "Fox"
    word2 = "Level"

    is_palindrome_1 = is_palindrome(word1)
    is_palindrome_2 = is_palindrome(word2)

    print("Is input_str_1 a palindrome?", is_palindrome_1)  # should be False
    print("Is input_str_2 a palindrome?", is_palindrome_2)  # should be True


def task_5():
    """
    Convert a camelCase string to a snake_case string
    """

    input_str = "thisIsCamelCase"

    result = ""

    expected = "this_is_camel_case"
    print("snake_case string: ", result)
    print(result == expected)  # should be True


def task_6():
    """
    Count the number of characters excluding spaces
    """

    sentence = "This is a sample sentence with spaces."

    char_count = 0

    expected = 31
    print("Number of characters excluding spaces:", char_count)
    print(char_count == expected)  # should be True


def task_7():
    """
    Remove all vowels from a string
    """

    input_str = "This is a sample sentence with vowels."

    result = ""

    expected = "Ths s  smpl sntnc wth vwls."
    print("String without vowels: ", result)
    print(result == expected)  # should be True


if __name__ == '__main__':
    # task_1()
    # task_2()
    # task_3()
    task_4()
    # task_5()
    # task_6()
    # task_7()