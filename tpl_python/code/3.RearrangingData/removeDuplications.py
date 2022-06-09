import json
import collections
with open("server/tpl_python/data_webcrawling/final_book_data.json", "r" ) as f:
    books = json.load(f)["books"]
links = []
for book in books:
    link = book["link"]
    links.append(link)
titles = []
for book in books:
    title = book["title"]
    titles.append(title)
# overlappedTitles = [item for item, count in collections.Counter(titles).items() if count > 1]

#.....only for DOUBLE counted titles!!.....
# lenOfBooks = len(books)
# for i in range(0, lenOfBooks):
#     print(books[i]['link'])
count = -1
lenOfBooks = len(books)
overlappedLinks = [item for item, count in collections.Counter(links).items() if count > 1]
for book in books:
    count += 1
    for overlappedLink in overlappedLinks:
        if book['link'] == overlappedLink:
            del books[count]
            overlappedLinks.remove(overlappedLink)

books = {"books": books}
with open("server/tpl_python/data_webcrawling/final_book_data(without_duplications).json", "w") as f:
    json.dump(books, f,indent=3, ensure_ascii=False)