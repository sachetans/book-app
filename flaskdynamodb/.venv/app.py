from flask import Flask, jsonify, request
# from aws_controller import *
import aws_controller


music = [{'id' : 1, 'name': 'nirvana'}, {'id' : 2, 'name': 'green day'}]

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the main page."
    
@app.route('/get-items')
def get_items():
    return jsonify(aws_controller.get_items())

@app.route('/get-book', methods=['GET'])
def get_book():
    book_id = request.args.get('id', type=int)
    name = request.args.get("name", type=str)
    # 1000, "Atomic habits"
    book = aws_controller.get_books(book_id, name)

    if book:
        return jsonify(book)

@app.route('/create-book', methods=['POST'])
def handle_post():
    data = request.get_json()
    jsonData = {
        "book_id" : data.get("book_id"),
        "title" : data.get("title"),
        "author" : data.get("author"),
        "isbn" : data.get("isbn"),
        "year_of_publication" : data.get("year_of_publication")
    }
    res = aws_controller.add_book('Books', jsonData)
    return jsonify(res)


if __name__ == '__main__':
    app.run()