import csv
import json
import random

def task_1() -> None:
    """
    Create a new file named "hello.txt" and write to it "Hello, world!".
    """
    with open("hello.txt", "w") as file:
        file.write("Hello, world!")

def task_2() -> None:
    """
    Open the file "hello.txt" and rewrite it with a random integer from the range [1, 10].
    """
    with open("hello.txt", "w") as file:
        file.write(str(random.randint(1, 10)))

def task_3() -> None:
    """
    Open file "hello.txt" and read the number from it to variable `n`. 
    Now append `n` upper-case letters starting with "A", "B", ... to the file.
    """
    with open("hello.txt", "r+") as file:
        n = int(file.read().strip())
        file.write("\n" + "".join(chr(65 + i) for i in range(n)))

def task_4() -> None:
    """
    Now open this file again and print to console its content.
    """
    with open("hello.txt", "r") as file:
        print(file.read())

def task_5() -> None:
    """
    Create a file `warehouse_v1.csv` and write the contents of `warehouse` list to it using `file.write()`.
    """
    warehouse = [
        {"product": "Apple", "price": 0.5, "quantity": 10},
        {"product": "Banana", "price": 0.75, "quantity": 20},
        {"product": "Orange", "price": 0.35, "quantity": 15}
    ]
    with open("warehouse_v1.csv", "w") as file:
        file.write("product,price,quantity\n")
        for item in warehouse:
            file.write(f"{item['product']},{item['price']},{item['quantity']}\n")

def task_6() -> None:
    """
    Use csv writer convenience methods to do the same to the file `warehouse_v2.csv`.
    """
    warehouse = [
        {"product": "Apple", "price": 0.5, "quantity": 10},
        {"product": "Banana", "price": 0.75, "quantity": 20},
        {"product": "Orange", "price": 0.35, "quantity": 15}
    ]
    with open("warehouse_v2.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["product", "price", "quantity"])
        writer.writeheader()
        writer.writerows(warehouse)

def task_7() -> None:
    """
    Store the same `warehouse` object to the `warehouse.json` file.
    """
    warehouse = [
        {"product": "Apple", "price": 0.5, "quantity": 10},
        {"product": "Banana", "price": 0.75, "quantity": 20},
        {"product": "Orange", "price": 0.35, "quantity": 15}
    ]
    with open("warehouse.json", "w") as file:
        json.dump(warehouse, file, indent=4)
