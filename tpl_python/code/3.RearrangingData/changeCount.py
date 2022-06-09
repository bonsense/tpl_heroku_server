from itertools import count
import json

filePath = "server/tpl_python/data_webcrawling/final_book_data(duplication_removed).json"
changing_key = "count"

with open (filePath, 'r') as f:
    datum = json.load(f)

TheMostUpperKey = list(datum.keys())[0]
datum = datum[TheMostUpperKey]
count = 0
for data in datum:
    data[changing_key] = count
    count += 1
    
datum = {TheMostUpperKey: datum}
with open(filePath, "w") as f:
    json.dump(datum, f,indent=3, ensure_ascii=False)
