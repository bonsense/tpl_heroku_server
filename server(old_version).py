from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
import json

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

with open("/Users/seumgminshin/Desktop/portfolio/lib/TPLkoreanbooks/server/tpl_python/data_webcrawling/final_book_data.json", 'r') as read_file:
    books = json.load(read_file)
books = books["books"]

def sort_by_category(category):
    if category == 'all':
        return(books)

    result_by_category = []
    for book in books:
        if book['category'] == category:
            result_by_category.append(book)
    return(result_by_category)

class Category(Resource):
    def get(self,category ):
        return(sort_by_category(category))

api.add_resource(Category, "/category/<string:category>")

if __name__ == "__main__":
	app.run(debug=True)