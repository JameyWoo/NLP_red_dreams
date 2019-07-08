# -*- encoding: utf-8 -*-

"""
@file: run.py
@time: 2019/7/8 9:47
@author: 姬小野
@version: 0.1
"""

import get_urls
import get_comments
import sentiment_analysis_test
from Filenames import Filenames


def init_one(version, id):  # 初始化版本信息与文件名格式. 一本书
    # version = 'v0.5'  # 添加版本
    # key = 'The+Tale+of+Genji'  # 源氏物语
    name = 'Dream+of+the+Red+Chamber'  # 红楼梦
    file = Filenames(version=version, id=id)
    # file.set_name(file.id2name(id))
    print("now: {}\n".format(file.name))
    return file


def run_one_book(file):
    # 获取评论页的urls
    request_urls = get_urls.get_source_urls(file.name)
    urls_set = set()
    for each in request_urls:
        get_urls.get_result_urls(each, urls_set)
    urls = list(urls_set)
    print("{} urls".format(len(urls)))
    print("---urls get down---\n")

    # 获取评论
    comments = get_comments.Comment()
    # get_comments(urls[1], comments=comments) # 测试一个url的爬取
    for i in range(len(urls)):
        print("-----第{}个url of {}: \"{}\"-----".format(i + 1, file.id, file.name.replace('+', ' ')))
        get_comments.get_comments(urls[i], comments)
    comments.write('src/%s_review_info.csv' % file.prefix)

    # 根据评论生成情感分析结果
    comments = comments.texts
    # print(comments)
    print(len(comments))
    analysis_results = sentiment_analysis_test.sent_analysis(comments)
    print(analysis_results)
    sentiment_analysis_test.write2file(analysis_results, file.prefix)
    print(len(analysis_results))


def run_all_books(version):
    for i in range(5, 7):  # 爬取所有或部分的书, 自己设定范围
        one_book = init_one(version=version, id=i)
        run_one_book(one_book)


def main():
    one_book = init_one(version='v0.6', id=-1)
    run_one_book(one_book)
    # run_all_books(version='v0.6')

if __name__ == "__main__":
    main()