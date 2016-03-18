from flask import Flask, request, render_template, make_response
from io import StringIO
import datetime

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("contents.html")

if __name__ == "__main__":
	app.run(debug=True)