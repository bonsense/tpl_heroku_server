import json

with open("server/tpl_python/data_webcrawling/final_book_data.json", "r" ) as f:
    books = json.load(f)


for book in books['books']:
    book['category'] = book['category'].replace('/', '+')

with open("server/tpl_python/data_webcrawling/final_book_data-2.json", "w") as f:
    json.dump(books, f,indent=3, ensure_ascii=False)
