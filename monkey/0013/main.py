# -*- coding:utf-8 -*-
from lxml import etree
import requests

__author__ = 'monkey'

# 题目要求：
# 用Pyhton写一个爬图片的程序，爬这个链接里的日本妹子图片
# 地址：http://tieba.baidu.com/p/2166231880

def spider(url):
    html = requests.get(url)
    print(html.text)

if __name__ == '__main__':
    url = "http://tieba.baidu.com/p/2166231880"
    spider(url)