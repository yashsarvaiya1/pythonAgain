from flask import Flask, jsonify, request
app = Flask(__name__)
books = [
    {"id": 1, "title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling"},
    {"id": 2, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 3, "title": "The Lord of the Rings", "author": "J.R.R. Tolkien"},
    {"id": 4, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 5, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 6, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
]

@app.route("/books",methods=["POST"])
def get_books():
    return jsonify(books)

@app.route("/books/<int:book_id>",methods=["POST"])
def get_book(book_id):
    book = [book for book in books if book["id"] == book_id]
    return jsonify(book or {"message": "Book not found"})

@app.route("/books/add",methods=["POST"])
def add_book():
    book = {
        "id": len(books) + 1,
        "title": request.json["title"],
        "author": request.json["author"],
    }
    books.append(book)
    return jsonify(book)

@app.route("/books/update/<int:book_id>",methods=["POST"])
def update_book(book_id):
    book = [book for book in books if book["id"] == book_id]
    book[0]["title"] = request.json["title"]
    book[0]["author"] = request.json["author"]
    return jsonify(book)

@app.route("/books/delete/<int:book_id>",methods=["POST"])
def delete_book(book_id):
    book = [book for book in books if book["id"] == book_id]
    books.remove(book[0])
    return jsonify(books)

if __name__ == "__main__":
    app.run(debug=True)