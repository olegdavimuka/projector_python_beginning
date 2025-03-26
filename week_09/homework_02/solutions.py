# assignment_9_2_stats.py
import timeit
from typing import List
import math

def mean(li: List[float]) -> float:
    return sum(li) / len(li)

def variance(li: List[float]) -> float:
    mu = mean(li)
    return sum((x - mu) ** 2 for x in li) / len(li)

def std(li: List[float]) -> float:
    return math.sqrt(variance(li))

def median(li: List[float]) -> float:
    li_sorted = sorted(li)
    n = len(li_sorted)
    mid = n // 2
    if n % 2 == 0:
        return (li_sorted[mid - 1] + li_sorted[mid]) / 2
    return li_sorted[mid]

def benchmark():
    stmt_mean_custom = 'mean(li)'
    stmt_mean_np = 'np.mean(arr)'

    stmt_var_custom = 'variance(li)'
    stmt_var_np = 'np.var(arr)'

    stmt_std_custom = 'std(li)'
    stmt_std_np = 'np.std(arr)'

    stmt_median_custom = 'median(li)'
    stmt_median_np = 'np.median(arr)'


    setup = '''
    import random
    import numpy as np
    from __main__ import mean, variance, std, median
    
    arr = np.random.rand(10_000) * 100
    li = [random.random() * 100 for _ in range(10_000)]
    '''

    custom_mean_time = timeit.timeit(stmt=stmt_mean_custom, setup=setup, number=10000, globals=globals())
    numpy_mean_time = timeit.timeit(stmt=stmt_mean_np, setup=setup, number=10000, globals=globals())

    custom_var_time = timeit.timeit(stmt=stmt_var_custom, setup=setup, number=10000, globals=globals())
    numpy_var_time = timeit.timeit(stmt=stmt_var_np, setup=setup, number=10000, globals=globals())

    custom_std_time = timeit.timeit(stmt=stmt_std_custom, setup=setup, number=10000, globals=globals())
    numpy_std_time = timeit.timeit(stmt=stmt_std_np, setup=setup, number=10000, globals=globals())

    custom_median_time = timeit.timeit(stmt=stmt_median_custom, setup=setup, number=10000, globals=globals())
    numpy_median_time = timeit.timeit(stmt=stmt_median_np, setup=setup, number=10000, globals=globals())

    print("\nTime per 10000 executions, secs")
    print("| Func   | Custom   | Numpy    |")
    print("|--------|----------|----------|")
    print(f"| mean   | {custom_mean_time:.2f} | {numpy_mean_time:.2f} |")
    print(f"| var    | {custom_var_time:.2f} | {numpy_var_time:.2f} |")
    print(f"| std    | {custom_std_time:.2f} | {numpy_std_time:.2f} |")
    print(f"| median | {custom_median_time:.2f} | {numpy_median_time:.2f} |")
