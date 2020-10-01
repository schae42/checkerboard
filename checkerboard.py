
from flask import Flask, render_template
app = Flask(__name__)

print(__name__)

@app.route('/')
def index_8_by_8():
    return render_template("index.html", x=8, y=8)

@app.route('/<x>')
def index_8_by_4():
    return render_template("index.html", x=int(x), y=8)

@app.route('/<x>/<y>')
def index_x_by_y(x, y):
    return render_template("index.html", x=int(x), y=int(y))

if __name__=="__main__":
    app.run(debug=True)