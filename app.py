from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    return 'Hello World!'


@app.route('/search')
def search4letter(phrase: str='the answer to everything and more', letters: str='aeiou') -> set:
    """Finds and returns the set of 'letters' found in 'phrase'"""
    return set(letters).intersection(set(phrase))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the deep Web')


app.run()
