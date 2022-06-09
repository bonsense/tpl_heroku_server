import json

with open ("/Users/minkijung/Desktop/tplkoreanbook/server/tpl_python/data_webcrawling/aladinlinks530.json", 'r') as f:
    links = json.load(f)

with open ("/Users/minkijung/Desktop/tplkoreanbook/server/tpl_python/data_webcrawling/googleSearchedTitles.json", 'r') as f:
    books = json.load(f)["books"]

books = books[2175: 3628]  #2175: 3628
result = books

for book in books:
    findLink = False
    for link in links:
        if book['link'] == link['tpl_link']:
            findLink = True
    if findLink:
        result.remove(book)

# for book in result:
#     print(book['original_title'])

# with open("/Users/minkijung/Desktop/tplkoreanbook/server/tpl_python/data_webcrawling/aladinUnsearchedData530.json", "w") as f:
#     json.dump(result, f,indent=3, ensure_ascii=False)
