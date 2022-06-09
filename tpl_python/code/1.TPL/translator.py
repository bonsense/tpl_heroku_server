from hangul_utils import join_jamos
from langdetect import detect
vowel = {
    'yae': 'ㅒ',
    'wae': 'ㅙ',
    'ae': 'ㅐ',
    'oe': 'ㅚ',
    'wi': 'ㅟ',
    'ya': 'ㅑ',
    'yŏ': 'ㅕ',
    'yo': 'ㅛ',
    'yu': 'ㅠ',
    'yŭ': 'ㅠ',
    'ye': 'ㅖ',
    'wa': 'ㅘ',
    'wŏ': 'ㅝ',
    'wǒ': 'ㅝ',
    'we': 'ㅞ',
    'ŭi': 'ㅢ',
    'a': 'ㅏ',
    'e': 'ㅔ',
    'ŏ': 'ㅓ',
    'o': 'ㅗ',
    'u': 'ㅜ',
    'ŭ': 'ㅡ',
    'i': 'ㅣ',
}
vowel2 = {
    'ㅏ': '',
    'ㅑ': '야',
    'ㅓ': '어',
    'ㅕ': '여',
    'ㅗ': '오',
    'ㅛ': '요',
    'ㅜ': '우',
    'ㅠ': '유',
    'ㅡ': '으',
    'ㅢ': '의',
    'ㅣ': '이',
    'ㅐ': '애',
    'ㅒ': '얘',
    'ㅔ': '에',
    'ㅖ': '예',
    'ㅙ': '왜',
    'ㅞ': '웨',
    'ㅚ': '외',
    'ㅟ': '위',
    'ㅘ': '와',
    'ㅝ': '워'
}
onset = {
    'n\'g': "ㄴㄱ",
    'nʻg': "ㄴㄱ",
    'ng': 'ㅇ',
    'kʻ': 'ㅋ',
    'kʼ': 'ㅋ',
    'k\'': 'ㅋ',
    'tʻ': 'ㅌ',
    'tʼ': 'ㅌ',
    't\'': 'ㅌ',
    'pʻ': 'ㅍ',
    'pʼ': 'ㅍ',
    'p\'': 'ㅍ',
    'chʻ': 'ㅊ',
    'ch\'': 'ㅊ',
    'chʼ': 'ㅊ',
    'kk': 'ㄲ',
    'tt': 'ㄸ',
    'pp': 'ㅃ',
    'ss': 'ㅆ',
    'tch': 'ㅉ',
    'ch': 'ㅈ',
    'j': 'ㅈ',
    'k': 'ㄱ',
    'g': 'ㄱ',
    't': 'ㄷ',
    'd': 'ㄷ',
    'p': 'ㅂ',
    'b': 'ㅂ',
    's': 'ㅅ',
    'h': 'ㅎ',
    'n': 'ㄴ',
    'm': 'ㅁ',
    'r': 'ㄹ',
    'l': 'ㄹ'   #need another rule for deromanization
}
key_vowel = list(vowel.keys())
val_vowel = list(set(vowel.values()))
key_onset = list(onset.keys())

f = open("tpl_title_NoTranslate.txt", 'r')
title = f.readlines()
f.close()

count = 0
for k in title:
    #trimming title
    original = k.replace('[', '').replace(']', '').replace('\n', '')
    k = k.lower()
    k = k.replace('ǒ', 'ŏ').replace('ǔ', 'ŭ').replace('ō', 'ŏ').replace("author", '').replace('ʻ', '\'').replace('ʼ', '\'')

    first_k = k.split(",", 1)[0]
    first_k = first_k.split("=", 1)[0]
    first_k = first_k.split(":", 1)[0]
    first_k = first_k.strip()
    first_k = first_k.replace('ǒ', 'ŏ').replace('ǔ', 'ŭ')

    #Only when the title is not English, translate the title
    if detect(first_k) != "en":
        vari = k.find('=')
        if vari != -1:
            k2 = k.split("=", 1)[1]
            k = k.split("=", 1)[0]
        shwi = k.find("shwi")
        if shwi != -1:
            k = k.replace("shwi", 'ㅅㅟ')

        for i in key_vowel:
            result = k.find(i)
            if result != -1:
                k = k.replace(i, vowel[i])
        for i in key_onset:
            result = k.find(i)
            if result != -1:
                k = k.replace(i, onset[i])
        k = join_jamos(k)
        for i in val_vowel:
            result = k.find(i)
            if result != -1:
                k = k.replace(i, "ㅇ" + i)
        if vari != -1:
            k = k + '=' + k2
        k = join_jamos(k)
        k = k.replace("y이", "이")
        k = k.replace("y이", '이')

    else:
        if first_k.find('ŏ') != -1 or first_k.find('ŭ') != -1:
            vari = k.find('=')
            if vari != -1:
                k2 = k.split("=", 1)[1]
                k = k.split("=", 1)[0]
            shwi = k.find("shwi")
            if shwi != -1:
                k = k.replace("shwi", 'ㅅㅟ')

            for i in key_vowel:
                result = k.find(i)
                if result != -1:
                    k = k.replace(i, vowel[i])
            for i in key_onset:
                result = k.find(i)
                if result != -1:
                    k = k.replace(i, onset[i])
            k = join_jamos(k)
            for i in val_vowel:
                result = k.find(i)
                if result != -1:
                    k = k.replace(i, "ㅇ" + i)
            if vari != -1:
                k = k + '=' + k2
            k = join_jamos(k)
            k = k.replace("y이", "이")
            k = k.replace("y이", '이')
            k = k.split("=", 1)[0]
        if first_k.find("\'") != -1:
            vari = k.find('=')
            if vari != -1:
                k2 = k.split("=", 1)[1]
                k = k.split("=", 1)[0]
            loc = first_k.index("\'")
            if first_k[loc + 1] != 's':
                shwi = k.find("shwi")
                if shwi != -1:
                    k = k.replace("shwi", 'ㅅㅟ')

                for i in key_vowel:
                    result = k.find(i)
                    if result != -1:
                        k = k.replace(i, vowel[i])
                for i in key_onset:
                    result = k.find(i)
                    if result != -1:
                        k = k.replace(i, onset[i])
                k = join_jamos(k)
                for i in val_vowel:
                    result = k.find(i)
                    if result != -1:
                        k = k.replace(i, "ㅇ" + i)
                if vari != -1:
                    k = k + '=' + k2
                k = join_jamos(k)
                k = k.replace("y이", "이")
                k = k.replace("y이", '이')
                k = k.split("=", 1)[0]
        if first_k.find('ʼ') != -1:
            vari = k.find('=')
            if vari != -1:
                k2 = k.split("=", 1)[1]
                k = k.split("=", 1)[0]
            loc2 = first_k.find('ʼ')
            if first_k[loc2 + 1] != 's':
                shwi = k.find("shwi")
                if shwi != -1:
                    k = k.replace("shwi", 'ㅅㅟ')

                for i in key_vowel:
                    result = k.find(i)
                    if result != -1:
                        k = k.replace(i, vowel[i])
                for i in key_onset:
                    result = k.find(i)
                    if result != -1:
                        k = k.replace(i, onset[i])
                k = join_jamos(k)
                for i in val_vowel:
                    result = k.find(i)
                    if result != -1:
                        k = k.replace(i, "ㅇ" + i)
                if vari != -1:
                    k = k + '=' + k2
                k = join_jamos(k)
                k = k.replace("y이", "이")
                k = k.replace("y이", '이')
                k = k.split("=", 1)[0]
    
    k = k.replace('[', '').replace('.', ' ').replace('-', ' ').replace(']', '').replace('\n', '').replace("우이", '의')
    result = k + "," + original + "\n"
    title[count] = result
    count += 1

title.sort()

with open("Translated_titles.txt", "w") as f:
    for element in title: 
        f.write(element)