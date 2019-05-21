from flask import Flask, render_template
from Rates import getRates
from Comments import getComments
from Abstract import getAbstract
from BasicInfo import getBasicInfo
from Score import getScore

app = Flask(__name__)

@app.route('/<article>')
def article(article):
    good_rate, mid_rate, bad_rate, all_comments = getRates(article)
    title = article
    abstract = getAbstract(article)
    comments = getComments(article)
    name, english_name, author = getBasicInfo(article)
    score = getScore(article)
    comment_type = ['好评', '差评', '中评']
    return render_template('article.html', **locals())

@app.route('/test')
def test():
    return "<h1>Hello, world</h1>"

@app.route("/")
def index():
    articles = ['红楼梦', '三国演义', '水浒传', '西游记']
    return render_template('index.html', articles=articles)

if __name__ == '__main__':
    app.run()