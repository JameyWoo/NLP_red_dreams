# -*- encoding: utf-8 -*-

"""
@file: run.py.py
@time: 2019/7/8 9:47
@author: 姬小野
@version: 0.1
"""

import get_urls
import get_comments
import sentiment_analysis_test
from Filenames import Filenames


def init():
    version = 'v0.5'  # 添加版本
    # key = 'The+Tale+of+Genji'  # 源氏物语
    name = 'Dream+of+the+Red+Chamber'  # 红楼梦
    file = Filenames(version=version, id=2)
    file.set_name(name)
    return file


def main():
    file = init() # 初始化版本信息与文件名格式

    # 获取评论页的urls
    request_urls = get_urls.get_source_urls(file.name)
    urls_set = set()
    for each in request_urls:
        get_urls.get_result_urls(each, urls_set)
    urls = list(urls_set)
    print("---urls get down---")

    # 获取评论
    comments = get_comments.Comment()
    # get_comments(urls[1], comments=comments) # 测试一个url的爬取
    for i in range(len(urls)):
        print("-----第{}个url-----".format(i + 1))
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


if __name__ == "__main__":
    main()