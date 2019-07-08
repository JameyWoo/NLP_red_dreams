# -*- encoding: utf-8 -*-

'''
:file: textblob_test.py
:time: 2019/7/6 23:44
:author: 姬小野
:version: 0.1
:desc:
nltk data github: https://github.com/nltk/nltk_data
离线安装: https://blog.csdn.net/zhangcucmb/article/details/80824231 # 一定要安装
'''

# TODO(Jamey): 写完代码
# todo注释可有意思

from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

blob = TextBlob(text)
blob.tags           # [('The', 'DT'), ('titular', 'JJ'),
                    #  ('threat', 'NN'), ('of', 'IN'), ...]

blob.noun_phrases   # WordList(['titular threat', 'blob',
                    #            'ultimate movie monster',
                    #            'amoeba-like mass', ...])

for sentence in blob.sentences:
    print(sentence.sentiment.polarity)
# 0.060
# -0.341

blob.translate(to="es")  # 'La amenaza titular de The Blob...'

print(blob.tags)