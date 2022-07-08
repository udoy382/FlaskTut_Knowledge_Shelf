from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'heyudoyrahman'


class InfoForm(FlaskForm):
    breed = StringField('What type of breed are you?')
    submit = SubmitField('submit')


class myInfoForm(FlaskForm):
    breed = StringField('What type of breed are you?', validators=[DataRequired()])
    mood = RadioField('Please select your choose: ', choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food = SelectField(u'Pick your choice: ', choices=[('chicken', 'Chicken'), ('fish', 'Fish'), ('veg', 'Grass')])
    feedback = TextAreaField()
    submit = SubmitField('submit')


@app.route("/")
def hello_world():
    return "<h1>Hello, Flask!</h1>"


@app.route("/info")
def info():
    return "<h1>Saifur Rahman udoy</h1>"


@app.route("/friend/<name>")
def friend(name):
    # return f"<h1>My Friend name is {name}</h1>"

    return 'last char of any name {}'.format(name[-1]) 


@app.route('/home')
def index():
    name = 'Saifur Rahman Udoy'

    list1 = list(name)

    dict1 = {'YouTube':'Knowledge Shelf'}

    return render_template('index.html', name=name, list1=list1, dict1=dict1)


@app.route('/home2')
def home2():
    # list1 = [1, 2, 3, 4, 5]
    list1 = ['Udoy', 'Mariyam', 'Fariha', 'Jara', 'Amy', 'Akhi', 'Mahima']

    return render_template('home2.html', list1=list1)


@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/friends/<name>')
def friends(name):
    return render_template('main.html', name=name)


# --------------html form code--------------

@app.route('/formhome')
def formhome():
    return render_template('formhome.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thankyou')
def thankyou():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('thankyou.html', first=first, last=last)


# ------------Error handler---------------

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# -------------New Form code--------------


@app.route('/flaskform', methods=['GET', 'POST'])
def flaskform():
    breed = False

    form = InfoForm()
    if form.validate_on_submit():
        breed = form.breed.data
        form.breed.data = ''

    return render_template('flaskform.html', form=form, breed=breed)


@app.route('/myinfoform', methods=['GET', 'POST'])
def myinfoform():
    myform = myInfoForm()

    if myform.validate_on_submit():

        session['breed'] = myform.breed.data
        session['mood'] = myform.mood.data
        session['food'] = myform.food.data
        session['feedback'] = myform.feedback.data

        return redirect(url_for('thankyou'))

    return render_template('index.html', myform=myform)



if __name__ == '__main__':
    app.run(debug=True)
