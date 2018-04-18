from flask import Flask, render_template, request
import os
import tweepy

app = Flask("MyApp")

# ADJUSTMENT: Read the mailgun secret key from config variables
mailgun_secret_key_value = os.environ.get('MAILGUN_SECRET_KEY', None)

# This is needed for Heroku configuration as in Heroku our
# app will porbably not run on port 5000 as Heroku will automatically
# assign a port for our application
port = int(os.environ.get("PORT", 5000))

@app.route("/")
def localhost():
	return render_template("index.html")

@app.route("/search", methods=['POST'])
def search():
	search_term = request.form['search']
	
	tweet_ids = fetch_twitter_data(search_term)
	return render_template("index.html", tweet_ids = tweet_ids)


def fetch_twitter_data(search_term):
#this is bad, move keys to config file
	consumer_key = "ZtB8cA3gacvGCcRRlg6gwGNsL"
	consumer_secret = "y5V6jWkTwN3isEpCuQZ8yyTkmgQqEfZRYRm91SnV2RlN2yiSBl"
	access_token = "1969091970-gDAwKNYC9lT8b1PuKJmmnQJ0V61e5CxtoOxoLh9"
	access_token_secret = "rDeFnM6UqlBLhZgErBVa9ro3huz9hCKbZQEue1zeKzPez"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	if (not api):
		print ("Problem connecting to API")

	results = api.search(q= search_term)

	tweet_ids = []

	for result in results: 
		tweet_ids.append(result.id)

	return tweet_ids

# ADJUSTMENT: Setup our application to run with the needed port.
app.run(host='0.0.0.0', port=port, debug=True)