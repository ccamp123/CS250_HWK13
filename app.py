from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__,static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


# class Ski(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     make = db.Column(db.String(20))
#     # model = db.Column(db.String(30))
#     # width = db.Column(db.Integer)
#     # length = db.Column(db.Integer)

@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/create')
def createPage():
    return render_template('create.html')
@app.route('/create',methods=['POST'])
def create():
    return 1
@app.route('/read')
def readPage():
    return render_template('read.html')

if __name__ == "__main__":
    app.run(debug=True)