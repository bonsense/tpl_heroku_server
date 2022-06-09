import json

TBS = [] #Title Before Search
CN = 4360 #Count Number (2175 -> 2902 ->  -> 4748) 
#... 700개 검색 다 끝나는 데 8분 걸림

fileObject = open("client/public/tpl_json.json", "r")
jsonContent = fileObject.read()
aList = json.loads(jsonContent)

for i in range(CN, 4748):
    adding_data = [aList['books'][0][i]['title'], aList['books'][0][i]['link']]
    TBS.append(adding_data)