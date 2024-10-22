from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/slider/GetSliders', methods=['GET'])
def GetSliders():
    data = [
        {"sliderId": 1, "name": "Object 1", "description": "This is the first object"},
        {"sliderId": 2, "name": "Object 2", "description": "This is the second object"},
        {"sliderId": 3, "name": "Object 3", "description": "This is the third object"}
    ]
    return jsonify(data)

@app.route('/about/GetAbout', methods=['GET'])
def GetAbout():

    data = {"name": "Object 1", "description": "And yes, this is the last block of representative placeholdercontent. Again, not really intended to be actually read, simply here to give you a better view of what this would look like with some actual content. Your content."}

    return jsonify(data)
@app.route('/products/MostSellProducts', methods=['GET'])
def MostSellProducts():

    data = [
        {"id": 1, "name": "Product 1", "description": "This is the first Product", "price": "120", "image":"photo-512.png"},
        {"id": 2, "name": "Product 2", "description": "This is the second Product", "price": "200", "image":"photo-512.png"},
        {"id": 3, "name": "Product 3", "description": "This is the third Product", "price": "550", "image":"photo-512.png"},
        {"id": 4, "name": "Product 4", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
    ]
    return jsonify(data)
@app.route('/products/GetProducts', methods=['GET'])
def GetProducts():

    data = [
        {"id": 1, "name": "Product 1", "description": "This is the first Product", "price": "120", "image":"photo-512.png"},
        {"id": 2, "name": "Product 2", "description": "This is the second Product", "price": "200", "image":"photo-512.png"},
        {"id": 3, "name": "Product 3", "description": "This is the third Product", "price": "550", "image":"photo-512.png"},
        {"id": 4, "name": "Product 4", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 5, "name": "Product 4", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 6, "name": "Product 4", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 7, "name": "Product 4", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 8, "name": "Product 4", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 9, "name": "Product 4", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 10, "name": "Product 4", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 11, "name": "Product 4", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 12, "name": "Product 4", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run()