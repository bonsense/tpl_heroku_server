import json
import collections

with open("server/tpl_python/data_webcrawling/final_book_data(중복된링크제거2).json", "r" ) as f:
    books = json.load(f)["books"]

links = []
for book in books:
    link = book["link"]
    links.append(link)

titles = []
for book in books:
    title = book["title"]
    titles.append(title)

overlappedlinks = [item for item, count in collections.Counter(links).items() if count > 1]
overlappedtitles = [item for item, count in collections.Counter(titles).items() if count > 1]

print(overlappedtitles)
print(overlappedlinks)