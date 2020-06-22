from flask import Flask, render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from forms import RegistrationForm, LoginForm, CycleForm

app = Flask(__name__, template_folder='../templates')
app._static_folder = '../static'
app.config['SECRET_KEY'] = 'daeb36b22d124c6abeb1483b2bb81455'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///SOX.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    name = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)


class TestModule(db.Model):
    TestId = db.Column(db.Integer, primary_key=True)
    Section = db.Column(db.String(250), nullable=False)
    Cycle = db.Column(db.String(250), nullable=False)
    Process = db.Column(db.String(250), nullable=False)
    Control = db.Column(db.String(250), nullable=False)
    Tester = db.Column(db.String(100), nullable=False)
    Reviewer = db.Column(db.String(100), nullable=False)
    Status = db.Column(db.String(100), nullable=False)
    Effect = db.Column(db.String(100), nullable=False)
    #Due = db.Column(db.DateTime, default=datetime.now)
    #DateComplete = db.Column(db.DateTime, default=datetime.now)
    TestData = db.Column(db.String(1000), nullable=False)
    Due = db.Column(db.String(100), nullable=False)
    DateComplete = db.Column(db.String(100), nullable=False)


db.create_all()

#db.drop_all()


names = [
    {
        'name': 'Edouard Roland',
    },

    {
        'name': 'Garfield Vernon',
    }
]


@app.route('/')
@app.route('/home')
def home():
    posts = TestModule.query.all()
    return render_template('home.html', title='home', posts=posts)  # render home template


@app.route('/page2')
def page2():
    return render_template('page2.html', title='page2')  # render home template


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


@app.route('/cycle', methods=['GET', 'POST'])
def cycle():
    form = CycleForm()
    if form.validate_on_submit():

        #time_in_duedate = datetime.strptime(form.duedate.data, "%d/%m/%Y")
        #time_in_completeddate = datetime.strptime(form.completeddate.data, "%d/%m/%Y")
        post = TestModule(Section=form.section.data, Cycle=form.cycle.data, Process=form.testprocess.data,
                          Control=form.control.data, Tester=form.tester.data, Reviewer=form.reviewer.data,
                          Status=form.status.data, Effect=form.effectiveness.data, TestData=form.testdesc.data,
                          Due=form.duedate.data, DateComplete=form.completeddate.data)
        db.session.add(post)
        db.session.commit()
        flash('Your entry has been saved', 'success')
        return redirect(url_for('home'))
    return render_template('cycle.html', title='Test Submission Form', form=form, legend='Test Submission Form')


@app.route('/displaycycle/<int:id>')
def displaycycle(id):
    post = TestModule.query.get_or_404(id)
    return render_template('displaycycle.html', title='Display Cycle', post=post)


@app.route('/displaycycle/<int:id>/update', methods=['GET', 'POST'])
def updatecycle(id):
    post = TestModule.query.get_or_404(id)
    form = CycleForm()
    #time_in_duedate = datetime.strptime(form.duedate.data, "%d/%m/%Y")
    #time_in_completeddate = datetime.strptime(form.completeddate.data, "%d/%m/%Y")
    if form.validate_on_submit():
        post.Section = form.section.data
        post.Cycle = form.cycle.data
        post.Process = form.testprocess.data
        post.Control = form.control.data
        post.Tester = form.tester.data
        post.Reviewer = form.reviewer.data
        post.Status = form.status.data
        post.Effect = form.effectiveness.data
        post.TestData = form.testdesc.data
        post.Due = form.duedate.data
        post.DateComplete = form.completeddate.data
        db.session.commit()
        flash('Cycle has been updated', 'success')
        return redirect(url_for('displaycycle', id=post.TestId))
    elif request.method == 'GET':
        form.section.data = post.Section
        form.cycle.data = post.Cycle
        form.testprocess.data = post.Process
        form.control.data = post.Control
        form.tester.data = post.Tester
        form.reviewer.data = post.Reviewer
        form.status.data = post.Status
        form.testdesc.data = post.TestData
        form.effectiveness.data = post.Effect
        form.duedate.data = post.Due
        form.completeddate.data = post.DateComplete
    return render_template('cycle.html', title='Update Cycle', form=form,
                           legend='Update Cycle')


@app.route('/calendar')
def calendar():
    return render_template('calendar.html', title='Calendar')  # render home template


if __name__ == '__main__':
    app.run(debug=True)
