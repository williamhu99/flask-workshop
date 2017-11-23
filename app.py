from flask import Flask, render_template
from lxml import html

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('main.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)