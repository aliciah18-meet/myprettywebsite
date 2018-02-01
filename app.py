
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./users.db'

db = SQLAlchemy(app)

 
class User(db.Model):
    __tablename__ = "users"
    id = db.Column (db.Integer, primary_key=True)
    user = db.Column(db.String(30),unique=True)
    password = db.Column(db.String(30),unique=True)
    def __init__(self, user, password):
    	self.user = user
    	self.password = password


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
		db.session.add(user)
		db.session.commit()
		return render_template('home2.html')



@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == "GET":
		return render_template('login.html')
	elif request.method == "POST":
		log_in=User.query.filter_by(user=request.form['username'], password=request.form['password']).first()
		
		if log_in == None:
			return render_template('login.html', log_in=False)
		else:
			return render_template('home2.html')


@app.route('/logout', methods=['GET'])
def logout():
	return render_template('home.html')



@app.route('/viewportfolio')
def view_portfolio():
	return render_template('viewportfolio.html')

@app.route('/viewportfolio2')
def view_portfolio2():
	return render_template('viewportfolio2.html')

@app.route('/makeportfolio')
def make_portfolio():
	return render_template('makeportfolio.html')

if __name__ == "__main__":
	app.debug = True
	app.run()
