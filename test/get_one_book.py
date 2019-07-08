'''
1. 首先获得search的页面, 从中提取出各种书籍的id
2. 实现翻页爬取更多页面, 但是页面多了, 结果会不准确且评论极少
3. 根据id构造出全部的url, 再进行下一步
'''

import requests
import re
from lxml import etree

headers={
    "User-Agent" : "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language" : "en-us",
    "Connection" : "keep-alive",
    "Accept-Charset" : "GB2312,utf-8;q=0.7,*;q=0.7"
}

key = 'The+Tale+of+Genji'
url = 'https://www.amazon.com/s?k=%s&page=1'%key

search_page = requests.get(url, headers=headers)

# with open("src/tmp/amazone_search.html", 'w+', encoding='utf-8') as file:
#     file.write(search_page.text)

html = etree.HTML(search_page.text)

result = html.xpath('//a[@class="a-size-base a-link-normal s-no-hover a-text-normal"]/@href')
print(len(result))

result_urls = []
for each in result:
    try:
        one_url = re.findall(r'dp/(.*)/ref', each)[0]
        result_urls.append(one_url)
    except:
        pass

print(result_urls)
print(len(result_urls))

review_url_src = "https://www.amazon.com/Tale-Genji-Shikibu-Murasaki/product-reviews/"

with open("src/reviews.txt", 'w+', encoding='utf-8') as review_file:
    review_file.write("")
with open("src/reviews.txt", 'a+', encoding='utf-8') as review_file:
    for each in result_urls:
        one_review_url = review_url_src + each
        review_file.write(one_review_url + '\n')