from flask import Flask,render_template
from forms import SignUpForm , LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'

pets=[{"id":1, "name":"Rocky", "description":"German Shephard"}]
users = [
            {"id": 1, "full_name": "Pet", "email": "t@pets.co", "password": "password"},
        ]
@app.route('/')
def home():
    user={'username':'namrata'}
    return render_template('home.html', user=user, pets=pets)

@app.route('/about')
def about():
    posts=['hello','post1','hello2']
    return render_template('about.html', posts=posts)

@app.route('/login')
def userLogin():
    return render_template('login.html')

@app.route("/signup",methods=["GET","POST"])
def Signup():
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = {"id": len(users)+1, "full_name": form.full_name.data, "email": form.email.data, "password": form.password.data}
        users.append(new_user)
        return render_template("signup.html", message = "Successfully signed up")
    return render_template("signup.html", form = form)

@app.route('/details/<int:id>')
def details(id):
    if pets[0]["id"]==id:
        return render_template('details.html', id=id, pet=pets[0])
    



if __name__ == "__main__":
    app.run(debug=True)
