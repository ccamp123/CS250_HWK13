from flask import Flask,render_template

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/create')
def createPage():
    return render_template('create.html')

@app.route('/read')
def readPage():
    return render_template('read.html')

app.run(debug=True)