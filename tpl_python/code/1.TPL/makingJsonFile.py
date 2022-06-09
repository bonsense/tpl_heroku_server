#-*- coding:utf-8 -*-
import json

with open("/data/Translated_titles.txt", 'r') as f:
    lines = f.readlines()

count = 1
data = []
category = [
                    "어린이",
                    "청소년",
                    "좋은부모",
                    "소설/시/희곡",
                    "에세이",
                    "인문학",
                    "사회과학",
                    "역사",
                    "과학",
                    "예술/대중문화",
                    "종교/역학",
                    "경제경영",
                    "자기계발",
                    "외국어",
                    "가정/요리/뷰티",
                    "건강/취미/레저",
                    "기타"]

for sample in lines:
    sample_split = sample.split(',')
    sample_split[-1] = sample_split[-1].strip()
    length_sample_split = len(sample_split)
    while length_sample_split < 4:
        sample_split.append("")
        length_sample_split += 1

    if sample_split[2]:
        link = "https://www.torontopubliclibrary.ca/search.jsp?Ntt={}".format(sample_split[2])
    else:
        link = "https://www.torontopubliclibrary.ca/search.jsp?Ntt={}".format(sample_split[0])
    
    newsample = {"count_number": count,
                 "title": sample_split[0],
                 "author": sample_split[1],
                 "title_original": sample_split[2],
                 "author_original": sample_split[3],
                 "cover": "https://image.aladin.co.kr/img/bn/wflash/2022/02/220509_ad05.png", #dummy img
                 "category": category[count % 17], #dummy category
                 "link": link}

    data.append(newsample)
    count += 1
    link = ''

data_structured = {"books": [data]}

with open("tpl_json.json", 'w', encoding='UTF-8') as f:
    json.dump(data_structured, f, indent=2, ensure_ascii=False)