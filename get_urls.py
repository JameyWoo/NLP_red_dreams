'''
# 根据get_one_book.py修改
1. 首先获得search的页面, 从中提取出各种书籍的id
2. 实现翻页爬取更多页面, 但是页面多了, 结果会不准确且评论极少
3. 根据id构造出全部的url, 再进行下一步
'''

import requests
import re
from lxml import etree

from Filenames import Filenames


def get_source_urls(key):
    '''
    获取源搜索页面的url, 分页
    :return:
    '''
    url = 'https://www.amazon.com/s?k=%s&page=' % key
    request_urls = []
    for i in range(1, 5):
        request_urls.append(url + str(i))
    return request_urls


def get_result_urls(one_source_url, urls_set):
    '''
    获取一个页面的urls的id, 组合拼接成评论页的url
    :param one_source_url: 一个页面的url
    :param urls_set: 维护的评论页的url的集合
    :return:
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us",
        "Connection": "keep-alive",
        "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7"
    }
    source = requests.get(one_source_url, headers=headers).text
    html = etree.HTML(source)
    results = html.xpath('//a[@class="a-size-base a-link-normal s-no-hover a-text-normal"]/@href')
    review_url_src = "https://www.amazon.com/Tale-Genji-Shikibu-Murasaki/product-reviews/"
    for each in results:
        try:
            one_url = review_url_src + re.findall(r'dp/(.*)/ref', each)[0]
            urls_set.add(one_url)
        except:
            pass


def save_urls(urls, filename="src/reviews_urls.txt"):
    '''
    保存评论的url, 可以自定义保存的位置
    :param urls:
    :param filename:
    :return:
    '''
    with open(filename, 'w+', encoding='utf-8') as file:
        for each in urls:
            file.writelines(each + '\n')


def init():
    version = 'v0.3'  # 添加版本
    # key = 'The+Tale+of+Genji'  # 源氏物语
    name = 'Dream+of+the+Red+Chamber'  # 红楼梦
    file = Filenames(version=version, id=1)
    file.set_name(name)
    return file


def main():
    file = init()

    request_urls = get_source_urls(file.name)
    # save_urls("src/%s_request.txt" % (version + key))
    urls_set = set()
    for each in request_urls:
        get_result_urls(each, urls_set)
    result_urls = list(urls_set)
    # 保存结果的url到文件中
    save_urls(urls=result_urls, filename="src/%s_reviews_urls.txt" % file.prefix)


if __name__ == "__main__":
    main()
