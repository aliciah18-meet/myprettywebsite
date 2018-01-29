
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'

db = SQLAlchemy(app)

 
class User(db.Model):
    __tablename__ = "users"
    id = db.Column (db.Integer, primary_key=True)
    user = db.Column(db.String(30),unique=True)
    passwrd = db.Column(db.String(30),unique=True)
    def __init__(self, user, passwrd):
    	self.user = user
    	self.passwrd = passwrd


db.create_all()

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
	if request.method == 'GET':
		return render_template('signup.html')
	elif request.method == 'POST':
		user= User(request.form['username'], request.form['password'])
		db.session.add(User)
		db.session.commit
		return render_template('home2.html')



@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == "GET":
		return render_template('login.html')
	elif request.method == "POST":
		session.query.User

		return render_template('home.html')

if __name__ == "__main__":
	app.debug = True
	app.run()