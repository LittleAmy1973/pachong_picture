from urllib import request

url = 'http://www.baidu.com'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

page = request.Request(url, headers=headers)

page_info = request.urlopen(url).read().decode('utf-8')
print(page_info)



'''
page_info = request.urlopen(url).read()
page_info = request.decode('utf-8')
'''