import numpy as np
import pandas as pd

def task1_create_arrays():
    res = np.array([1, 2, 3, 4, 5])
    res2 = np.arange(1, 6)
    return res, res2

def task2_random_2d_array():
    return np.random.randint(1, 101, size=(3, 5))

def task3_first_row(array):
    return array[0]

def task4_last_column(array):
    return array[:, -1]

def task5_column_stats(array):
    col = array[:, 1]  # second column (index 1)
    return col.min(), col.max(), col.sum()

def task6_tabulate_exp():
    x = np.arange(0, 1.01, 0.1)
    f_x = np.exp(2 * x)
    return f_x

def task7_load_titanic():
    url = "https://web.stanford.edu/class/cs102/datasets/Titanic.csv"
    return pd.read_csv(url)

def task8_inspect_data(df):
    return df.columns, df.head(10)

def task9_add_fullname(df):
    df["full name"] = df["first"] + " " + df["last"]
    return df

def task10_remove_names(df):
    df.drop(columns=["first", "last"], inplace=True)
    return df

def task11_total_survivors(df):
    return df[df["survived"] == 1].shape[0]
