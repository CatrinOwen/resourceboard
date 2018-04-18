from flask import Flask, render_template, request

app = Flask("MyApp")

@app.route("/form")
def form():
	return render_template("form.html")

@app.route("/signup", methods=['POST'])
def sign_up():
	form_data = request.form

	name = form_data["fullname"]
	email = form_data["email"]

	print name
	print email

	return "Yay awesome job"

app.run(debug=True)