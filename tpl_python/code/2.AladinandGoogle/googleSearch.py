import requests
from bs4 import BeautifulSoup
import json
import re
import constant

unsearched_titles = []
results = []
count = constant.CN #Count Number
booktitle_aladin = ''
booktitle_kyobo = ''

for title in constant.TBS:  #TBS= Titles before search
    link = title[1] #link to TPL website
    title = title[0] #title for searching
    try:
        # Searching title on Google and getting html text into soup
        # Num=40 ... meaning that showing 40 results
        url = "https://www.google.com/search?q={}".format(title)
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"}
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        #Find all h3 tags and filter with the keyword '알라딘'
        search_result = soup.body.find_all('h3')
        for bookInfo in search_result:
            if bookInfo.findAll(text=re.compile('알라딘')):
                booktitle = bookInfo
                if booktitle:
                    booktitle = booktitle.get_text()
                    booktitle_aladin = booktitle.replace(" - 알라딘", '').replace("[전자책]", '').replace("[중고]", '').replace("(양장)", '').strip()
                    pass
            elif bookInfo.findAll(text=re.compile('교보문고')):
                booktitle2 = bookInfo
                if booktitle2:
                    booktitle2 = booktitle2.get_text()
                    booktitle_kyobo = booktitle2.replace("교보문고", '').replace("전자책", '').replace("중고", '').replace("양장본", '').strip()
                    pass
        #If the title is not founded, add the title to the unsearched list
        if booktitle_aladin == '' and booktitle_kyobo == '':
            unsearched_titles.append(title)
        #Append titles into results
        adding_data = {
            "count": count,
            "original_title": title,
            "aladin_title": booktitle_aladin,
            "kyobo_title": booktitle_kyobo,
            "link": link
            }
        results.append(adding_data)
        booktitle_aladin = ''
        booktitle_kyobo = ''
        print("%d th search" %count)
        count = count + 1
    #Error handling... If google blocks me, then break the for loop and save data into files
    except Exception as e:
        print(e)
        print("error on %d" %count)
        break

with open("server/tpl_python/data_webcrawling/googleSearchedTitles.json", "r") as j:
    data = json.loads(j.read())

data = data["books"]
for result in results:
    data.append(result)
data = {"books": data}

with open("server/tpl_python/data_webcrawling/googleSearchedTitles.json", "w") as j:
    json.dump(data, j, indent=3, ensure_ascii=False)

