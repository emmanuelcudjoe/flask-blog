from flask import Flask, flash, render_template, url_for, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = 'b4f76fd343dd06aec49ab3d7bb6d81f3'

posts = [
    {
        "author": "Joe Regan",
        "title": "Blog post 1",
        "content": "First post content",
        "date_posted": "June 13, 2022"
    },
    {
        "author": "Sammy Johnson",
        "title": "Blog post 2",
        "content": "Second post content",
        "date_posted": "June 12, 2022"
    },
    {
        "author": "Jane Doe",
        "title": "Blog post 3",
        "content": "Third post content",
        "date_posted": "June 14, 2022"
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)