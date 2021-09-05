from flask import Flask, render_template
from flask.wrappers import Response
import requests

app = Flask(__name__)

blog_url = 'https://api.npoint.io/2cc4964fbf14d756832e'


@app.route('/')
def index():
    response = requests.get(url=blog_url)
    blog_data = response.json()
    return render_template('index.html', posts=blog_data)


@app.route('/post/<blog_id>')
def post(blog_id):
    response = requests.get(url=f'{blog_url}/{blog_id}')
    blog_data = response.json()
    print(blog_data)
    return render_template('post.html', post=blog_data)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
