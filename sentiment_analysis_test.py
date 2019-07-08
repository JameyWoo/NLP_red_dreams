# -*- encoding: utf-8 -*-

"""
@file: sentiment_analysis_test.py
@time: 2019/7/6 23:16
@author: 姬小野
@version: 0.1
@desc: None
"""

import csv
from textblob import TextBlob

from Filenames import Filenames


def get_comments(filename):
    '''
    从文件中获取评论列表
    :param filename: 指定文件名
    :return:
    '''
    with open(filename, 'r', encoding='utf-8') as csv_file:
        reader = csv_file.readlines()
        # print(reader)
    return [each.split(',')[2] for each in reader][1:]


def get_one_analysis(one_comment):
    '''
    获取一个评论的分析结果
    :param one_comment:
    :return:
    '''
    text = TextBlob(one_comment)
    return text.sentiment.polarity


def sent_analysis(comments):
    '''
    评论的情感分析
    :param comments: 传入的评论列表
    :return: 返回情感分析值列表
    '''
    analysis_results = []
    for each in comments:
        analysis_results.append(get_one_analysis(each))
    return analysis_results


def write2file(analysis_results, source_file_prefix):
    '''将情感分析的结果写入到新的csv文件中'''
    with open('src/%s_review_info.csv' % source_file_prefix, 'r', encoding='utf-8') as csv_read:
        rows = csv.reader(csv_read)
        with open('src/%s_review_sentiment.csv' % source_file_prefix, 'w', encoding='utf-8', newline='') as csv_write:
            writer = csv.writer(csv_write)
            writer.writerow(['id', 'star', 'sentiment', 'text'])
            rows_list = []
            for each in rows:
                rows_list.append(each)
            rows_list = rows_list[1:]
            for i in range(len(rows_list)):
                rows_list[i][2:2] = [analysis_results[i]] # 很巧妙的插入元素的方法
                writer.writerow(rows_list[i])


def main(file):
    comments = get_comments('src/%s_review_info.csv' % file.prefix) # 一个评论的列表
    # print(comments)
    print(len(comments))
    analysis_results = sent_analysis(comments)
    print(analysis_results)
    write2file(analysis_results, file.prefix)
    print(len(analysis_results))


if __name__ == "__main__":
    file = Filenames('Dream+of+the+Red+Chamber', 'v0.2')
    main(file)