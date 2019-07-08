# -*- encoding: utf-8 -*-

'''
:file: get_comments.py
:time: 2019/7/5 22:23
:author: 姬小野
:version: 0.1
:desc: None
'''

import re
import csv
import requests
from lxml import etree

from Filenames import Filenames


class Comment:
    '''
    一个评论类, 包含一个评论的各种信息, 如:
    评论文本, 评论星级, 评论
    '''
    def __init__(self):
        '''
        评论的文本, 星级
        '''
        self.texts = []
        self.stars = []

    def __str__(self):
        '''
        :return: 返回 count of comments: $count
        '''
        str1 = "count of comments: %s\n"%str(len(self.texts))
        return str1

    def write(self, filename):
        '''
        将评论信息全部写入文件
        :param filename: 可以自己指定文件名
        :return:
        '''
        with open(filename, "w", encoding='utf-8', newline='') as csv_file:
            # 加一个newline参数, 否则csv文件会出现空行
            writer = csv.writer(csv_file)
            writer.writerow(['id', 'star', 'text'])
            rows = zip(range(len(self.texts)), self.stars, self.texts)
            writer.writerows(rows)
        print('---print down---')


def get_urls(filename):
    '''
    从txt中获取review的urls
    :param filename:
    :return: urls列表
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [each.replace("\n", '') for each in lines]


def get_comments(one_url, comments):
    '''
    从一个url网页获取评论
    :param one_url: 指定url
    :param comments: 传递过来的Comment类
    :return:
    '''
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1.6) ",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us",
        "Connection": "keep-alive",
        "Accept-Charset": "GB2312,utf-8;q=0.7,*;q=0.7"
    }
    try:
        source = requests.get(one_url, headers=headers, timeout=3).text
        html = etree.HTML(source)
        # print(source)
        tmp_url = one_url[-10:]
        print(tmp_url)
        with open("src/tmp/%s.html" % tmp_url, 'w+', encoding='utf-8') as file:
            file.write(source)
        file.close()
        results = html.xpath('//div[@class="a-row a-spacing-small review-data"]/span/span/text()')
        # 一个star的问题还没有解决
        stars = re.findall(r'title="(.*) out of 5 stars"', source)
        print(stars)
        print("len of results: ", len(results)) # TODO: 好像这里都错了, 一个页面最多只有十个评论啊.
        print("len of stars: ", len(stars))
        for i in range(len(results)):
            comments.texts.append(results[i].replace('\n', ' '))
            comments.stars.append(0)
        print(comments)
    except:
        pass
    return


def init():
    # 我觉得我需要写一个类来描述根据版本而改变的文件名, 而不是每次靠这种字符串拼接
    version = "v0.3"
    name = 'Dream+of+the+Red+Chamber'  # 红楼梦
    file = Filenames(version=version, id=1)
    file.set_name(name)
    return file


def main():
    file = init()

    urls = get_urls(filename="src/%s_reviews_urls.txt" % file.prefix)
    comments = Comment()
    # get_comments(urls[1], comments=comments) # 测试一个url的爬取
    for i in range(len(urls)):
        # TODO: 我是不是忘记了在一个评论url上翻页?
        print("-----第{}个url of {}-----".format(i + 1, file.name))
        get_comments(urls[i], comments)
    comments.write('src/%s_review_info.csv' % file.prefix)


if __name__ == "__main__":
    main()