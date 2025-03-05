from time import time

def task_1() -> None:
    """
    Write a decorator that ensures a function is only called by users with a specific role.
    Each function should have an user_type with a string type in kwargs.
    """
    def role_required(role: str):
        def decorator(func):
            def wrapper(*args, **kwargs):
                if kwargs.get("user_type") == role:
                    return func(*args, **kwargs)
                return "Access denied"
            return wrapper
        return decorator

    @role_required("admin")
    def admin_panel(**kwargs):
        return "Admin panel"

    @role_required("user")
    def user_panel(**kwargs):
        return "User panel"

    print(admin_panel(user_type="admin"))
    print(user_panel(user_type="user"))
    print(admin_panel(user_type="user"))
    print(user_panel(user_type="admin"))


def task_2() -> None:
    """
    Write a decorator that wraps a function in a try-except block and prints an error if any type of error has happened.
    """
    def error_handler(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error occurred: {e}")
        return wrapper

    @error_handler
    def divide(a: int, b: int) -> float:
        return a / b

    divide(5, 0)
    divide(5, 2)

def task_3() -> None:
    """
    Create a decorator that will check types. It should take a function with arguments and validate inputs with
    annotations. It should work for all possible functions. Don`t forget to check the return type as well
    """
    def type_check(func):
        def wrapper(*args, **kwargs):
            for arg, value in zip(func.__code__.co_varnames, args):
                if not isinstance(value, func.__annotations__.get(arg)):
                    raise TypeError(f"Invalid type for {arg}")
            result = func(*args, **kwargs)
            if not isinstance(result, func.__annotations__.get("return")):
                raise TypeError("Invalid return type")
            return result
        return wrapper

    @type_check
    def add(a: int, b: int) -> int:
        return a + b

    @type_check
    def divide(a: int, b: int) -> float:
        return a / b

    print(add(5, 7))
    print(divide(5, 2))
    print(add(5, "7"))
    print(divide(5, "2"))


def task_4() -> None:
    """
    Create a function that caches the result of a function, so that if it is called with the same argument
    multiple times, it returns the cached result first instead of re-executing the function.
    """
    def cache(func):
        cached = {}
        def wrapper(*args, **kwargs):
            if args not in cached:
                print("Adding to cache")
                cached[args] = func(*args, **kwargs)
            return cached[args]
        return wrapper

    @cache
    def add(a: int, b: int) -> int:
        return a + b

    print(add(5, 7))
    print(add(5, 7))


def task_5() -> None:
    """
    Write a decorator that adds a rate-limiter to a function, so that
    it can only be called a certain amount of times per minute
    """
    def rate_limiter(limit: int):
        def decorator(func):
            last_called = 0
            call_count = 0

            def wrapper(*args, **kwargs):
                nonlocal last_called, call_count
                current_time = time()
                if current_time - last_called >= 60:
                    last_called = current_time
                    call_count = 0
                if call_count >= limit:
                    print("Rate limit exceeded")
                    return
                call_count += 1
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @rate_limiter(2)
    def add(a: int, b: int) -> int:
        return a + b

    print(add(5, 7))
    print(add(5, 7))
    print(add(5, 7))