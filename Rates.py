# 生成分数, 好评，差评，中评
import json

def getRates(article):
    with open('./static/jsons/%s.json'%article, 'r', encoding='utf-8') as file:
        json_file = file.read()
    data = json.loads(json_file)
    pos, neg, mid = data['positive'], data['negative'], data['middle']
    alll = (pos + neg + mid) / 100
    return round(pos/alll, 2), round(neg/alll, 2), round(mid/alll, 2), int(alll*100)