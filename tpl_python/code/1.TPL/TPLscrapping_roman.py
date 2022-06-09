import requests
from bs4 import BeautifulSoup

book_list = []
for i in range(0,87):
    #get HTML files from TPL website... 'NO={50*i}' means pages number
    url = "https://www.torontopubliclibrary.ca/search.jsp?Erp=50&N=37906+38221&No={}&Ntk=Keyword_Anywhere&advancedSearch=true".format(50*i)
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"}
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    books = soup.find_all("div", attrs={"class": "description small-9 medium-10 columns"}) #save all title info in books(list)
    for book in books: #a book contains a single book info
        insideList = []
        book_title = book.find("span", attrs={"class": "notranslate"}) #notranslate title
        if book_title:
            book_title = book_title.get_text().replace("/", '').replace(',', '.').strip()
            insideList.append(book_title)
            book_author = book.find("span", attrs={"class": "author"})
            if book_author:
                book_author = book_author.get_text().replace("/", '').replace('\n', '').replace(' ', '').replace(',', '.').strip()
                insideList.append(book_author)
                book_list.append(insideList)
    print("page %d is done" %i)

with open("tpl_title_NoTranslate.txt", "w") as f:
    book_list.sort()
    for element in book_list:
        temp = ''
        i = 0
        for inside in element:
            if i != 1:
                temp = temp + "[" + inside + ", "
                i= i+1
            else:
                temp = temp + inside + "]"
        f.write(temp + '\n')