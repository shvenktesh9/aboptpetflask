from flask import Flask
from flask.templating import render_template
app = Flask(__name__)

@app.route('/')
def home():
    user={'username':'namrata'}
    return render_template('home.html', user=user)

@app.route('/about')
def about():
    posts=['hello','post1','hello2']
    return render_template('about.html', posts=posts)

@app.route('/login')
def userLogin():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
