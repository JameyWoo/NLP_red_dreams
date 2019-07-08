import re

text = '''
/Tale-Genji-Illustrated-Murasaki-Shikibu-ebook/dp/B007NUIK8Y/ref=sr_1_17
'''

result = re.findall(r'dp/(.*)/ref', text)
print(result)