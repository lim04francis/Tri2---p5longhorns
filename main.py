

# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__)

#connects default URL of server to a python function
@app.route('/')
@app.route('/home')
def home():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("home.html")

@app.route('/cubism')
def cubism():
    return render_template("cubism.html")

@app.route('/photography')
def photography():
    return render_template("photography.html")

@app.route('/Movies')
def Movies():
    return render_template("Movies.html")

@app.route('/music')
def Music():
    return render_template('Music.html', genremain="")

@app.route("/Genresearch1", methods=["GET", "POST"])
def genresearch():
    if request.method == "POST":
        form= request.form
        Genre1 = form['MusicG1']
        return render_template('/music.html', genremain=Genre1)

@app.route('/paintingdescriptions')
def paintingdescriptions():
    return render_template("paintingdescriptions.html")

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True, port='3000', host='127.0.0.1')
