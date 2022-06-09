import json
with open("server/tpl_python/data_webcrawling/googleSearchedTitles.json", 'r') as f:
    googleDatum = json.load(f)['books']
with open("server/tpl_python/data_webcrawling/final_unsearched_links.json", 'r') as f:
    originalDatum = json.load(f)['unsearched_books']
with open("server/tpl_python/data_webcrawling/final_book_data.json", 'r') as f:
    finalDatum = json.load(f)['books']
with open("server/tpl_python/data_webcrawling/final_book_data(duplication_removed).json", 'r') as f:
    finalDatumDR = json.load(f)['books']

for finaldata in finalDatum:
    for originaldata in googleDatum:
        if (finaldata['link'] == originaldata['link']):
            googleDatum.remove(originaldata)
            break
for finaldata in finalDatumDR:
    for originaldata in googleDatum:
        if (finaldata['link'] == originaldata['link']):
            googleDatum.remove(originaldata)
            break

for finaldata in finalDatum:
    for originaldata in googleDatum:
        if (finaldata['title'] == originaldata['original_title']) or (finaldata['title'] == originaldata['aladin_title']) or (finaldata['title'] == originaldata['kyobo_title']):
            googleDatum.remove(originaldata)
            break
for finaldata in finalDatumDR:
    for originaldata in googleDatum:
        if (finaldata['title'] == originaldata['original_title']) or (finaldata['title'] == originaldata['aladin_title']) or (finaldata['title'] == originaldata['kyobo_title']):
            googleDatum.remove(originaldata)
            break

for finaldata in finalDatum:
    for originaldata in googleDatum:
        if (finaldata['title'].split('(')[0].split(':')[0].strip() == originaldata['original_title'].split(':')[0].split('(')[0].strip()) or (finaldata['title'].split('(')[0].split(':')[0].strip() == originaldata['aladin_title'].split(':')[0].split('(')[0].strip()) or (finaldata['title'].split('(')[0].split(':')[0].strip() == originaldata['kyobo_title'].split(':')[0].split('(')[0].strip()):
            googleDatum.remove(originaldata)
            break
for finaldata in finalDatumDR:
    for originaldata in googleDatum:
        if (finaldata['title'].split(':')[0].split('(')[0].split(',')[0].strip() == originaldata['original_title'].split(':')[0].split('(')[0].strip()) or (finaldata['title'].split(':')[0].split('(')[0].split(',')[0].strip() == originaldata['aladin_title'].split(':')[0].split('(')[0].strip()) or (finaldata['title'].split(':')[0].split('(')[0].split(',')[0].strip() == originaldata['kyobo_title'].split(':')[0].split('(')[0].strip()):
            googleDatum.remove(originaldata)
            break

print(len(googleDatum))
googleDatum = {"unsearched_books": googleDatum}
with open("server/tpl_python/data_webcrawling/final_unsearched_links.json", 'w') as f:
    json.dump(googleDatum, f, indent=3, ensure_ascii=False)
