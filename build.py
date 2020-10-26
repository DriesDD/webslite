from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<page>')
def blogs(page):
    pagedetails = next(i for i in PAGES if i[0] == page)
    return render_template('layout.html', article = pagedetails[1], title=pagedetails[2])

PAGES = [
    ['website','/articles/website.html','A website'],
    ['about','/articles/about.html','About Dries Makes'],
    ['poem','/articles/poem.html','A poem']
]

app.run(debug=True) 