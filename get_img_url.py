import requests
import re
import string

#定义获取网页内容的函数
def get_content(url):
	res_txt = requests.get(url)
	res = res_txt.content
	return res

#不同网页中的图片url不同，同一个网页中的也不同，要进行
#多次匹配才能全部提取出来，下面写了两个比较有代表性的
#网站的提取方法，但是仍然未能完全提取，还需要再写匹配
#规则。

#该函数使用http://www.baidu.com页面测试来提取的
def get_img_url1(url):
	comp = re.compile(r'(url\([\\h].*?\.(jpg|png|gif))')
	pipei = comp.findall(get_content(url))
	lis = []
	for i in pipei:
		a = string.replace(i[0],'\\/','/')
		b = re.search(r'(.*//)(.*)',a)
		if b != None:
			lis.append(b.group(2))
	return lis

#该函数使用http://www.sina.com页面来提取的
def get_img_url2(url):
	comp = re.compile(r'(http://.+?\.(jpg|png|gif))')
    try:
        pipei = comp.findall(get_content(url))
    except requests.exceptions.MissingSchema:
        raise TypeError('You should search url like this:(http://exmaple.com)')

	lis = []
	for i in pipei:
		a = re.search(r'(src=\")(http://.+?\.(jpg|png|gif))',i[0])
		if a == None:
			lis.append(i)
		else:
			lis.append(a.group(2))
	return lis

#print get_img_url1('http://www.baidu.com')
#print get_img_url2('http://www.hao123.com')
