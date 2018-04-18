import json
import requests

from flask import Flask, render_template, request


mailgun_domain = "https://api.mailgun.net/v3/sandbox587a15fcbb434b62982671111db56cbf.mailgun.org/messages"
your_email_address = "catza4eva@gmail.com"

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

app = Flask("MyApp")

@app.route("/")
def hello():
    return render_template("index.html")

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

app.run(debug=True)