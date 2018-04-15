from flask import Flask, render_template, request

app = Flask("MyApp")

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