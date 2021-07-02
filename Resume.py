from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime
import json

with open('C:\\Users\\Arushsi\\Desktop\\Resume Flask\\config.json','r') as f:
    params =  json.load(f)["params"]
local_server=True


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:@localhost/resume'
db=SQLAlchemy(app)

class Achievements(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    company_certificate = db.Column(db.String(120),  nullable=False)
    certificate_name = db.Column(db.String(120),  nullable=False)
    slug = db.Column(db.String(40),  nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=False)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(21),  nullable=False)
    phn_no = db.Column(db.String(12),  nullable=False)
    msg = db.Column(db.String(240), nullable=False)
    date = db.Column(db.String(6), nullable=True)
    
class Projects(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(140),  nullable=False)
    project_description = db.Column(db.String(500),  nullable=False)

@app.route("/")
def home():
    return render_template('index.html',params=params)

@app.route("/about")
def about():
    return render_template('about.html',params=params)


@app.route("/education")
def education():
    return render_template('education.html',params=params)

@app.route("/software_competencies")
def software_competencies():
    return render_template('software_competencies.html',params=params)


@app.route("/interests")
def interests():
    return render_template('interests.html',params=params)


@app.route("/projects")
def projects():
    return render_template('projects.html',params=params)

@app.route("/skills")
def skills():
    return render_template('skills.html',params=params)


@app.route("/achievements")
def achievements():
    
    return render_template('achievements.html',params=params)

@app.route("/contact",methods=['GET','POST'])
def contact():
    if(request.method=='POST'):
        '''Fetch data and add it to the database'''
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')

        entry=Contacts(name=name, email=email,phn_no=phone,msg=message,date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        

    return render_template('contact.html',params=params)



app.run(debug=True)