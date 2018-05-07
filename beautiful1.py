from urllib import request
from bs4 import BeautifulSoup

url = r'https://book.douban.com/'

headers = {'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read()
page_info = page_info.decode('utf-8')

soup = BeautifulSoup(page_info, 'html.parser')

titles = soup.find_all('h4','title')

'''
try:
    file = open(r'F:\Python\4week-study\pchong\title.txt','w')
    for title in titles:
        file.write(title.string + '\n')

finally:
    if file:
        file.close()

'''

with open(r'F:\Python\4week-study\pchong\title1.txt','w') as file:
    for title in titles:
        file.write(title.string + '\n')


