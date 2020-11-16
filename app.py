from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__,static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Ski(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(20))
    model = db.Column(db.String(30))
    width = db.Column(db.Integer)
    length = db.Column(db.Integer)

db.create_all()
@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/create')
def createPage():
    return render_template('create.html')
@app.route('/create',methods=['POST'])
def create():
    tempMake = request.form['Make']
    tempModel = request.form['Model']
    tempWidth = request.form['Width']
    tempLength = request.form['Length']
    tempSki = Ski(make=tempMake,model=tempModel,width=tempWidth,length=tempLength)
    db.session.add(tempSki)
    db.session.commit()
    return render_template('create.html')

@app.route('/read')
def readPage():
    resultsList = Ski.query.all()
    return render_template('read.html', results=resultsList)

@app.route('/update/<n>')
def updatePage(n):
    updateItem = Ski.query.filter_by(id=n).first()
    return render_template('update.html',u=updateItem,updateId=n)   
@app.route('/update/<n>',methods=['POST'])
def update(n):
    temp = Ski.query.filter_by(id=n).first() 
    temp.make = request.form['make']
    temp.model = request.form['model']
    temp.width = request.form['width']
    temp.length = request.form['length']   
    db.session.add(temp)
    db.session.commit()
    return redirect('/read')
@app.route('/delete/<n>')
def deleteEntry(n):
    tempDel = Ski.query.filter_by(id=n).first()
    db.session.delete(tempDel)
    db.session.commit()
    return redirect('/read')
if __name__ == "__main__":
    app.run(debug=True)