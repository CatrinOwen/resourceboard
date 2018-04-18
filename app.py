from flask import Flask, render_template
import os

app = Flask("MyApp")

# ADJUSTMENT: Read the mailgun secret key from config variables
mailgun_secret_key_value = os.environ.get('MAILGUN_SECRET_KEY', None)

# This is needed for Heroku configuration as in Heroku our
# app will porbably not run on port 5000 as Heroku will automatically
# assign a port for our application
port = int(os.environ.get("PORT", 5000))

port = int(os.environ.get("PORT", 5000))

@app.route("/localhost.py")
def localhost():
	return render_template("index.html")

@app.route("/search")
def search():
	search_term = form_data

	fetchtwitterdata(search_term)
	fetchnewsdata(search_term)

def fetch_twitter_data(search_term)
	data = request (url)

#not sure if the below is needed??
app.run(debug=True)

# ADJUSTMENT: Setup our application to run with the needed port.
app.run(host='0.0.0.0', port=port, debug=True)