"""app.py: render and route to webpages"""
from flask import request, render_template, redirect, url_for
from sqlalchemy import insert, text, select

from db.server import app
from db.server import db

from db.schema.post import Post


# create a webpage based off of the html in templates/index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/baseFile')
def baseFile():
        return render_template("baseFile.html")

@app.route('/templates/')
def baseFile2():
    return render_template("baseFile2.html")

@app.route('/home')
def Home():
     return render_template('home.html')

@app.route('/home2')
def Home2():
     
          with app.app_context():
               ps = select(Post)
               all_posts = db.session.execute(ps)

               return render_template('home2.html', posts=all_posts)
          return render_template('home2.html')

@app.route('/signup')
def signup():
     return render_template('signup.html')

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

