# -*- encoding: utf-8 -*-

'''
:file: Filenames.py
:time: 2019/7/7 9:37
:author: 姬小野
:version: 0.1
:desc: None
'''


class Filenames:
    '''统一不同版本, 不同文件的文件名类, 使其更简洁, 有组织.'''
    def __init__(self, version, id):
        """
        1. 没有将边城放进去, 因为搜到的条目实在是太少而且很多错误的
        2. 暂时莫言的作品也没放进去, 因为需要很多的筛选. 比如<<丰乳肥臀>>, 有很多sex内容.
        """
        self.name2id = { # 书名: 编号 的字典
            'The+Tale+of+Genji': 0,  # 源氏物语
            'Dream+of+the+Red+Chamber': 1,  # 红楼梦
            'Romance+of+the+Three+Kingdoms': 2,  # 三国演义
            'Outlaws+of+the+Marsh': 3,  # 水浒传
            'Journey+to+the+West': 4,  # 西游记
            'Rickshaw+Boy': 5,  # 骆驼祥子
            'Dawn+Blossoms+Plucked+at+Dusk': 6,  # 朝花夕拾, 看了看, 基本上没有人买啊, 也没有人评论
        }
        self.id = id
        self.name = list(self.id2name(id))[0]  # 如果没有指定name, 那么根据id默认得到第一个找到的名字
        self.version = version
        self.prefix = str(self.version) + '_' + str(self.id) # 调整顺序, 版本号应该先放在前面啊

    def __str__(self):
        str1 = str(self.name2id)
        str2 = "\nversion: " + str(self.version)
        return str1 + str2

    def id2name(self, id):
        '''从id得到书的名字'''
        # filter是过滤函数, 依次把函数作用于迭代器的每个元素, 如果满足, 则保留元素
        # names = filter(lambda x: x[1] == id, self.name2id.items())
        # return names  # 返回一个迭代器
        names = []
        for each in self.name2id.items():
            if each[1] == id:
                names.append(each[0])
        return names


    def set_name(self, name):
        self.name = name


def main():
    file1 = Filenames("The+Tale+of+Genji", 'v0.1')
    print(file1)
    names = file1.id2name(1)
    for each in names:
        print(each)


if __name__ == '__main__':
    main()