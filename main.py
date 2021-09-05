from flask import Flask, render_template, request
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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        print(f"Name: {request.form['name']}, "
              f"Email address: {request.form['email']}, "
              f"Phone Number: {request.form['phone']}, "
              f"Message: {request.form['message']}")
        return render_template('contact.html', message_sent=True)
    return render_template('contact.html', message_sent=False)


if __name__ == '__main__':
    app.run(debug=True)
