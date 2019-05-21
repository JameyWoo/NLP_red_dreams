# 得到评价，三种评价各三条，格式如[[0, 1, 2], [], []]
# 其中，中等评价可能不足三条
import pickle

def getComments(article):
    pickle_file = open("./static/pickles/%s.pkl"%article, 'rb')
    comments = pickle.load(pickle_file)
    return comments