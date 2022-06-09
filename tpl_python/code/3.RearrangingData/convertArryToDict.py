import json

with open ("server/tpl_python/data_webcrawling/googleSearchedTitles.json", 'r') as f:
    aList = json.loads(f.read())["books"]

result = []
for items in aList:
    data = {
        "count": items[0],
        "original_title": items[1],
        "aladin_title": items[2],
        "kyobo_title": items[3]
    }
    result.append(data)

result = {"books": result}

with open("googleSearchedTitles(수정2).json", 'w', encoding='UTF-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)