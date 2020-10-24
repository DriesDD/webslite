from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<page>')
def blogs(page):
    index = PAGES.index(page) + 1
    return render_template('layout.html', title=PAGES[index][1])

FILES = [
    '/articles/website.html',
    '/articles/else.html'
]
TITLES = [
    'A website',
    'Something else'
]

PAGES = [
    'website',['/articles/website.html','A website'],

]

app.run(debug=True) 