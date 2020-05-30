from flask import Flask, render_template
from newsapi import NewsApiClient



app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key="89978371303b45eb819a53f77fc04e5d")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])

    mylist = zip(news, desc, img)

    return render_template('index.html', context = mylist)

@app.route('/bbc')
def bbc():
        newsapi = NewsApiClient(api_key="89978371303b45eb819a53f77fc04e5d")
        topheadlines = newsapi.get_top_headlines(sources="bbc-news")

        articles = topheadlines['articles']

        desc = []
        news = []
        img = []

        for i in range(len(articles)):
            myarticles = articles[i]

            news.append(myarticles['title'])
            desc.append(myarticles['description'])
            img.append(myarticles['urlToImage'])

        mylist = zip(news, desc, img)

        return render_template('bbc.html', context = mylist)



if __name__ == "__main__":
    app.run(debug=True)
