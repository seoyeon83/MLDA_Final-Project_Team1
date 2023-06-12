from InterparkCrawling import *

info = pandas.read_csv('../../data/musical_crawling_info/musical_info_sy.csv', encoding='utf-8-sig')

title = info['title']
code = info['code']
th = info['th']

for i in range(len(title))[44:] :
    print(title[i], th[i])
    IPCrawling(code[i], title[i], th[i])