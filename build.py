from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/articles/home.html', article = '/articles/home.html', title='home')

@app.route('/<page>')
def article(page):
    pagedetails = next(i for i in PAGES if i[0] == page)
    nextdetails = PAGES[(PAGES.index(pagedetails) -1) % pagecount]
    prevdetails = PAGES[(PAGES.index(pagedetails) +1) % pagecount]
    return render_template(pagedetails[1],
    article = pagedetails[1], title=pagedetails[2], 
    nexttitle=nextdetails[2], nexturl=nextdetails[0],
    prevtitle=prevdetails[2], prevurl=prevdetails[0])

#every page is listed here as [URL resource name, HTML file path, title]
PAGES = [
    ['website','/articles/website.html','A website',''],
    ['about','/articles/about.html','About'],
    ['poem','/articles/poem.html','A poem']
]
pagecount = len(PAGES)

app.run(debug=True)