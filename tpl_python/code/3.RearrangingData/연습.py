import json
import collections

with open("server/tpl_python/data_webcrawling/final_book_data(중복된링크제거).json", "r" ) as f:
    books = json.load(f)["books"]

link_titles_duplicated = []

for link_title in link_titles_duplicated:
    for book in books:
        if book['title'] == link_title:
            books.remove(book)
            break


books = {"books": books}
with open("server/tpl_python/data_webcrawling/final_book_data(중복된링크제거2).json", "w") as f:
    json.dump(books, f,indent=3, ensure_ascii=False)