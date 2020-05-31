from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", message="Hello Flask!", contacts = ['c1', 'c2', 'c3', 'c4', 'c5']) 

@app.route("/mdb")
def mdb_index():
    return render_template("mdb.html", message="Message from Flask using Jinja Template") 

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
