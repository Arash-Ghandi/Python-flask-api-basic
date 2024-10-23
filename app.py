from flask import Flask,jsonify,request
from flask_cors import CORS
import math
import random

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

    data = GetItems()[0:4]

    return jsonify(data)
@app.route('/products/GetProducts', methods=['GET'])
def GetProducts():
    pageId = request.args.get('pageId')
    totalItems = len(GetItems())
    itemPerPage = 8
    activePage = int(pageId)
    pageCount = math.ceil(totalItems / itemPerPage)
    startIndex = (activePage - 1) * itemPerPage
    endIndex = min(startIndex + itemPerPage , totalItems)
    slicedItems = GetItems()[startIndex:endIndex]
    data = {
        "pageCount" : pageCount,
        "activePage" : activePage,
        "startIndex" : startIndex,
        "endIndex" : endIndex,
        "products" : slicedItems,
    }

    return jsonify(data)
    
@app.route('/products/GetProduct/<int:id>', methods=['GET'])
def GetProduct(id):
    product = [item for item in GetItems() if item['id'] == id]
    if len(product) > 0:
        product = product[0]
    
    return jsonify(product)
    
@app.route('/products/SuggestedProducts', methods=['GET'])
def GetSuggestProducts():
    suggestedItems = random.sample(GetItems(), 4)
    
    return jsonify(suggestedItems)

def GetItems():
    data = [
        {"id": 1, "name": "Product 1", "description": "This is the first Product", "price": "120", "image":"photo-512.png"},
        {"id": 2, "name": "Product 2", "description": "This is the second Product", "price": "200", "image":"photo-512.png"},
        {"id": 3, "name": "Product 3", "description": "This is the third Product", "price": "550", "image":"photo-512.png"},
        {"id": 4, "name": "Product 4", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 5, "name": "Product 5", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 6, "name": "Product 6", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 7, "name": "Product 7", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 8, "name": "Product 8", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 9, "name": "Product 9", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 10, "name": "Product 10", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 11, "name": "Product 11", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 12, "name": "Product 12", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 13, "name": "Product 13", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 14, "name": "Product 14", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 15, "name": "Product 15", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 16, "name": "Product 16", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 17, "name": "Product 17", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 18, "name": "Product 18", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 19, "name": "Product 19", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 20, "name": "Product 20", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
        {"id": 21, "name": "Product 21", "description": "This is the Product", "price": "50", "image":"photo-512.png"},
    ]

    return data

if __name__ == '__main__':
    app.run()