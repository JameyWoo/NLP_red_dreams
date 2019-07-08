# -*- encoding: utf-8 -*-

"""
@file: 获取指定value值的key测试.py
@time: 2019/7/8 12:51
@author: 姬小野
@version: 0.1
"""


def main():
    dict = { # 书名: 编号 的字典
        'The+Tale+of+Genji': 0,  # 源氏物语
        'Dream+of+the+Red+Chamber': 1,  # 红楼梦
        'Romance+of+the+Three+Kingdoms': 2,  # 三国演义
        'Outlaws+of+the+Marsh': 3,  # 水浒传
        'Journey+to+the+West': 4,  # 西游记
    }
    names = []
    id = 2
    for each in dict.items():
        if each[1] == id:
            names.append(each[0])
    print(names)
    return names


if __name__ == "__main__":
    main()