import requests

SERVER_URL = "http://127.0.0.1:5000"


def search_books():
    print("\nSearch books by author or title")
    search_type = input("Search by (1) Author or (2) Title: ").strip()

    if search_type == "1":
        author = input("Enter author name: ").strip()
        response = requests.get(f"{SERVER_URL}/books", params={"author": author})
    elif search_type == "2":
        title = input("Enter book title: ").strip()
        response = requests.get(f"{SERVER_URL}/books", params={"title": title})
    else:
        print("Invalid option.")
        return

    if response.status_code == 200:
        books = response.json()
        print("\nBooks found:")
        for book in books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}")
    else:
        print("No books found.")


def rent_book():
    print("\nRent a book")
    book_id = input("Enter book ID: ").strip()
    start_date = input("Enter start date (YYYY-MM-DD): ").strip()
    end_date = input("Enter end date (YYYY-MM-DD): ").strip()

    response = requests.post(f"{SERVER_URL}/rent", json={
        "id": int(book_id),
        "start_date": start_date,
        "end_date": end_date
    })

    print(response.json()["message"])


if __name__ == "__main__":
    while True:
        print("\nLibrary Client")
        print("1. Search books")
        print("2. Rent a book")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            search_books()
        elif choice == "2":
            rent_book()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")
