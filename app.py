from flask import Flask, render_template, request
import os
import tweepy
import json
import requests

mailgun_domain = "https://api.mailgun.net/v3/sandbox587a15fcbb434b62982671111db56cbf.mailgun.org/messages"
your_email_address = "catza4eva@gmail.com"




app = Flask("MyApp")

# ADJUSTMENT: Read the mailgun secret key from config variables

config_file = 'config.json'

def my_key():
    with open(config_file) as f:
        config = json.load(f)
    return config["mailgun_api_key"]


def send_simple_message(subject):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox587a15fcbb434b62982671111db56cbf.mailgun.org/messages",
        auth=("api", my_key()),
        data={
          "from": "Resource Board <catrin_owen@hotmail.com>".format(mailgun_domain),
          "to": [your_email_address],
          "subject": subject,
          "text": "You are now tuned in for search trends from across our database! Resource Board HQ"
        }
    )

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


@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/signup", methods=["POST"])
def handle_signup_form():
 
    form_data = request.form
 
    name_from_form = form_data["fullname"]

    subject_for_email = "Welcome to the Resource Board family, {}".format(name_from_form)

    send_simple_message(subject_for_email)

    return "You have been subscribed, thanks {}!".format(name_from_form)

# ADJUSTMENT: Setup our application to run with the needed port.
app.run(host='0.0.0.0', port=port, debug=True)