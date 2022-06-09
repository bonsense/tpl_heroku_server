import requests
from bs4 import BeautifulSoup

book_list = []
for i in range(0, 1):
    #get HTML files from TPL website... 'NO={50*i}' means pages number
    url = "https://www.torontopubliclibrary.ca/search.jsp?Erp=50&N=38221&No={}&Ntk=Keyword_Anywhere&advancedSearch=true".format(50*i)
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"}
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    books = soup.find_all("div", attrs={"class": "title align-top"})#save all title info in books(list)
    for book in books: #a book contains a single book info
        book_title = book.find("span", attrs={"class": "title_full_non_roman"}) #korean(or chiness) title

        if book_title:
            book_title = book_title.get_text().replace("/", '').strip()
            book_title = book_title.split("=", 1)
            book_title = book_title[0]
            book_titles_en = book.find_all("span", attrs={"class": "notranslate"})
            print(book_titles_en[0].get_text())

            #Run below code if you want to get Romanization titles as well
            for book_title_en in book_titles_en:
                book_title_en_parent = book_title_en.parent.parent
                if book_title_en_parent.find("div", attrs={"class": "title align-top"}):
                    book_title_en = book_title_en.get_text().replace("/", '').strip()
                    book_title_en = book_title_en.split("=", 1)
                    book_title_en = book_title_en[0]

                    book_title = book_title.split(":", 1)
                    book_title_en = book_title_en.split(":", 1)

                    temp_tutple = (book_title[0], book_title_en[0])
                    book_list.append(temp_tutple)
                    if (len(book_title) == 2) and (len(book_title_en) == 2):
                        temp_tutple = (book_title[1], book_title_en[1])
                        book_list.append(temp_tutple)
    print("page %d is done" %i)

with open("tpl_title.txt", "w") as f:
    for element in book_list:
        for element in element:
            f.write(element + '\n')
