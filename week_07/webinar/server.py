from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

books = [
    {"id": 1, "author": "Jack London", "title": "The Call of the Wild", "rented_dates": []},
    {"id": 2, "author": "Jack London", "title": "White Fang", "rented_dates": []},
    {"id": 3, "author": "Jack London", "title": "The Sea-Wolf", "rented_dates": []},
    {"id": 4, "author": "George Orwell", "title": "1984", "rented_dates": []},
    {"id": 5, "author": "George Orwell", "title": "Animal Farm", "rented_dates": []},
]

@app.route("/books", methods=["GET"])
def get_books():
    author = request.args.get("author")
    title = request.args.get("title")

    filtered_books = [
        {"id": book["id"], "author": book["author"], "title": book["title"]}
        for book in books
        if (author and book["author"].lower() == author.lower()) or
           (title and book["title"].lower() == title.lower())
    ]

    if filtered_books:
        return jsonify(filtered_books), 200
    return jsonify({"message": "No books found"}), 404

@app.route("/rent", methods=["POST"])
def rent_book():
    data = request.get_json()
    book_id = data.get("id")
    start_date = data.get("start_date")
    end_date = data.get("end_date")

    try:
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        return jsonify({"message": "Invalid date format. Use YYYY-MM-DD"}), 400

    for book in books:
        if book["id"] == book_id:
            for period in book["rented_dates"]:
                period_start = datetime.strptime(period["start_date"], "%Y-%m-%d")
                period_end = datetime.strptime(period["end_date"], "%Y-%m-%d")

                if not (end_date < period_start or start_date > period_end):
                    return jsonify({"message": "The book is already rented for these dates"}), 400

            book["rented_dates"].append({"start_date": data["start_date"], "end_date": data["end_date"]})
            return jsonify({"message": "Book rented successfully"}), 200

    return jsonify({"message": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
