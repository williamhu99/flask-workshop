from flask import Flask, render_template
from lxml import html
import requests
import json

app = Flask(__name__)

def getData():
	# gets data from https://api.github.com/events"
	data = requests.get("https://api.github.com/events")

	# converts to json dictionary
	jsonified = data.json()

	push_events_ct = 0
	other_events_ct = 0

	for entry in jsonified:
		if entry.get('type') == 'PushEvent':
			push_events_ct += 1
		else:
			other_events_ct += 1

	return [push_events_ct, other_events_ct]

@app.route("/")
def main():
	return render_template('main.html', values=[10,20,30], labels=["Ten","Twenty","Thirty"])

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)