import requests
from bs4 import BeautifulSoup
import json

titlesBeforeSearch = []
unsearched_titles = []
results = []
count = 0
unsearched_count = 0
searched_count = 0

linksOfBooks = [
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=170658040",
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=206425240",
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=155390621",
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=136536411",
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=16614423",
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=93211062",
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=10109",
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=38456523",
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=34614869",
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=8471071",
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=42297",
   "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=48506"]

for link in linksOfBooks:
    try:
        # Searching title on Google and get html text into soup
        url = link
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"}
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        try: 
                title = soup.body.find('a', attrs={'class': 'Ere_bo_title'}).get_text().replace('[세트]', '').replace('[eBook]', '').strip()
                author = soup.body.find('a', attrs={'class': 'Ere_sub2_title'}).get_text()
                cover =  soup.body.find('img', attrs={'id': 'CoverMainImage'}).get("src")
                category = soup.body.find('ul', attrs={'id': 'ulCategory'}).find_all('a')[1].get_text()
        except:
                pass

        adding_data = {
            "count": count, 
            "title": title, 
            "author": author, 
            "category": category, 
            "cover": cover}
        
        results.append(adding_data)
        print("%dth search is done" %count)
        count = count + 1
        title, author, cover, category = "","","","장르미상"

    except Exception as e:
        print(e)
        print("error")
        unsearched_titles.append(link)
        continue


with open("server/tpl_python/data_webcrawling/aladinReSearchedData.json", "w") as j:
    json.dump(results, j, indent=3, ensure_ascii=False)
