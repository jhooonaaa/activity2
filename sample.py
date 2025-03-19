import feedparser
from flask import Flask, render_template

app = Flask(__name__)
# bbc_feed = "http://feeds.bbci.co.uk/news/rss.xml"
rss_feeds = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'philstar': 'https://www.philstar.com/rss/headlines',
             'inquirer': 'https://www.inquirer.net/fullfeed',
            'rappler': 'https://www.rappler.com/feed/'}

@app.route("/")
@app.route("/bbc")
def bbc_news():
    return get_new('bbc')

@app.route("/cnn")
def cnn_news():
    return get_new('cnn')

@app.route("/fox")
def fox_news():
    return get_new('fox')

@app.route("/philstar")
def philstar_news():
    return get_new('philstar')

@app.route("/inquirer")
def inquirer_news():
    return get_new('inquirer')

@app.route("/rappler")
def rappler_news():
    return get_new('rappler')

def get_new(publication):
    feed = feedparser.parse(rss_feeds[publication])
    print(feed)
    article = feed['entries']
    print(article)
    return render_template("sample.html", Article = feed['entries'])


if __name__ == '__main__':
    app.run(port=5000, debug=True)