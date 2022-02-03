from flask import Flask,render_template
from datetime import datetime

year = datetime.now().year

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",year=year)

if __name__ == "__main__":
    app.run(debug=True)