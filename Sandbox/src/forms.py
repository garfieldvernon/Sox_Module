from flask_wtf import FlaskForm, validators
from wtforms import StringField, SubmitField, BooleanField, PasswordField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import DateField
from wtforms_sqlalchemy.fields import QuerySelectField


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = StringField('Password',
                           validators=[DataRequired()])
    submit = SubmitField('Sign up')
    remember = BooleanField('Remember Me')


class CycleForm(FlaskForm):
    section = StringField('Owner Organization',
                          validators=[DataRequired()])
    cycle = SelectField('Cycle Name', validators=[DataRequired()]
                        , choices=[('0', ''), ('1', 'Global Access Management'), ('2', 'Change Management')])
    testprocess = StringField('Process', validators=[DataRequired()])
    control = StringField('Control Activity Id', validators=[DataRequired()])
    tester = SelectField("Tester's Name", validators=[DataRequired()]
                         , choices=[('0', 'TBD'), ('1', 'Edouard Roland'), ('2', 'Garfield Vernon')])
    reviewer = SelectField("Reviewer's Name", validators=[DataRequired()]
                           , choices=[('0', 'TBD'), ('1', 'Edouard Roland'), ('2', 'Garfield Vernon')])
    testdesc = TextAreaField('Test Description', validators=[DataRequired()])
    status = SelectField('Test Execution Status', validators=[DataRequired()]
                         , choices=[('0', 'Open'), ('1', 'Completed'), ('2', 'In Progress')])
    effectiveness = SelectField('Test Execution Effectiveness', validators=[DataRequired()]
                        , choices=[('0', ''), ('1', 'Pass'), ('2', 'Fail')])
    # duedate = DateField('Due date', format='%Y/%m/%d')
    duedate = StringField('Due Date', validators=[DataRequired()])
    completeddate = StringField('Date Completed')
    submit = SubmitField('Submit')
