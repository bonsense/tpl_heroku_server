import requests
from bs4 import BeautifulSoup
import json

titlesBeforeSearch = []
linksOfBooks = []
unsearched_titles = []
results = []
count = 0
unsearched_count = 0
searched_count = 0

#Fetching titles from json file
with open ("/Users/minkijung/Desktop/tplkoreanbook/server/tpl_python/data_webcrawling/googleSearchedTitles.json", 'r') as f:
    aList = json.loads(f.read())["books"]

#Select the best title among three choice
lenOfaList = len(aList)
startingNumber = 4360  # 2175-> 4360
for i in range(startingNumber, lenOfaList):
    if aList[i]['aladin_title']:
        titlesBeforeSearch.append([aList[i]['aladin_title'], aList[i]['link'], aList[i]['original_title'], aList[i]['aladin_title'], aList[i]['kyobo_title']])
    elif aList[i]['kyobo_title']:
        titlesBeforeSearch.append([aList[i]['kyobo_title'], aList[i]['link'], aList[i]['original_title'], aList[i]['aladin_title'], aList[i]['kyobo_title']])
    else:
        titlesBeforeSearch.append([aList[i]['original_title'], aList[i]['link'], aList[i]['original_title'], aList[i]['aladin_title'], aList[i]['kyobo_title']])


for title in titlesBeforeSearch:
    original_title = title[2]
    aladin_title = title[3]
    kyobo_title = title[4]
    tpl_link = title[1]
    title = title[0]
    try:
        # Searching title on Google and get html text into soup
        url = "https://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord={}".format(title)
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"}
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        search_result = soup.body.find('div', attrs={"class": "ss_book_box"})
        try: 
            search_result.find('a', attrs={'class': 'bo3'})
            link = search_result.find('a', attrs={'class': "bo3"})
            link = link.get("href")
            link_data = {
                "count": searched_count, 
                "original_title": original_title, 
                "link": link, 
                "tpl_link":tpl_link}
            linksOfBooks.append(link_data)
            searched_count += 1
            link_data = {}
        except:
            link_data2 = {
                "count": unsearched_count, 
                "original_title": original_title, 
                "aladin_title": aladin_title,
                "kyobo_title": kyobo_title,
                "tpl_link": tpl_link}
            unsearched_titles.append(link_data2)
            unsearched_count += 1
            link_data2 = {}
        print("%dth search is done" %count)
        count += 1
    except Exception as e:
        print(e)
        print("error on %d" %count)
        break

# update links of books
with open("server/tpl_python/data_webcrawling/aladinLinksOfBooks.json", "r") as j:
    data = json.loads(j.read())
data = data["links"]
for link in linksOfBooks:
    data.append(link)
data = {"links": data}
with open("server/tpl_python/data_webcrawling/aladinLinksOfBooks.json", "w") as j:
    json.dump(data, j, indent=3, ensure_ascii=False)

#update unsearched data
with open("server/tpl_python/data_webcrawling/aladinUnsearchedData.json", "r") as j:
    data2 = json.loads(j.read())
data2 = data2["unsearched_title"]
for title in unsearched_titles:
    data2.append(title)
data2 = {"unsearched_title": data2}
with open("server/tpl_python/data_webcrawling/aladinUnsearchedData.json", "w") as j:
    json.dump(data2, j, indent=3, ensure_ascii=False)
