from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import csv
import json
from os import listdir

def getComments(filename): # 获取评论列表、评论中所有的单词，以空格分隔
    comments = np.zeros(0)
    words = ''
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        comments = [row[1] for row in reader][1:]
    for each in comments:
        words += each
    replace_list = [',', '.', '\'', '\"']
    for each in replace_list:
        words = words.replace(each, ' ')
    return comments, words

def getWordCloud(text_str, picture_name): # 生成词云
    reps = ['book', 'one', 'Chinese', 'story']
    for each in reps:
        text_str = text_str.replace(each, '')
    wordcloud = WordCloud(background_color="white",width=1980, height=1080, margin=2, random_state=42).generate(text_str)
    wordcloud.to_file(picture_name)
    return

def getJson(filename, infomation): # 写入json
    with open('./static/jsons/' + filename.replace('.csv', '.json'), 'w', encoding='utf-8') as jfile:
        jfile.write(json.dumps(infomation, indent=1))
    return

def get_p_or_n(comments, filename): # 获取情绪极化评分，并划定阈值确定是积极、消极或中立
    file = open('./static/csvs/' + filename, encoding='utf-8') # 解决路径中含中文的问题
    csvfile = pd.read_csv(file, encoding='utf-8')
    comments = csvfile['comment']
    stars = csvfile['star']
    star_cnt = [0]*5
    for each in stars:
        star_cnt[int(each) - 1] += 1
    scores = []
    results = []
    positive, middle, negative = 0, 0, 0
    infomation = {}
    pos_comments = []
    neg_comments = []
    mid_comments = []

    # 遍历评论，提取信息
    for each in comments:
        judge = TextBlob(each)
        # print(each)
        result = ''
        score = judge.sentiment.polarity
        if score > 0:
            positive += 1
            result = '积极'
            if len(pos_comments) < 3:
                if len(each) > 100:
                    pos_comments.append(each)
        elif score < 0:
            negative += 1
            result = '消极'
            if len(neg_comments) < 3:
                if len(each) > 100:
                    neg_comments.append(each)
        else:
            middle += 1
            result = '中立'
            if len(mid_comments) < 3:
                if len(each) > 100:
                    mid_comments.append(each)
        scores.append(score)
        results.append(result)
    comments_3 = [pos_comments, neg_comments, mid_comments]

    # 将三种评论用列表的方式存进pickle文件中
    pkl_file = open('./static/pickles/%s'%filename.replace('.csv', '.pkl'), 'wb')
    pickle.dump(comments_3, pkl_file)
    pkl_file.close()

    # 分析评论，将各级评分results、scores写入到csv文件中
    csvfile.insert(1, 'scores', scores)
    csvfile.insert(1, 'results', results)
    stars = csvfile.pop('star')
    csvfile.insert(1, 'stars', stars)
    csvfile.to_csv('./static/csvs/' + filename.replace('.csv', '_result.csv'), encoding='utf-8')
    stars = star_cnt
    # print(stars)

    # 将一些数量值写入到json文件中
    infomation = {'positive': positive, 'negative': negative, 'middle': middle, 'star1': stars[0],\
                  'star2': stars[1], 'star3': stars[2], 'star4': stars[3], 'star5': stars[4]}
    getJson(filename, infomation)
    return

def main():
    articles = ['红楼梦', '三国演义', '水浒传', '西游记']
    for bookname in articles:
        filename = bookname + ".csv"
        comments, words = getComments('./static/csvs/' + filename)
        print(len(comments))
        getWordCloud(words, "./static/wordclouds/wordcloud_of_%s.png"%bookname)
        get_p_or_n(comments, filename)

if __name__ == "__main__":
    main()