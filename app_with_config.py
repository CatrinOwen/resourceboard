import os
from flask import Flask

app = Flask ('ResourceBoard')

config_file = 'config.json'

if not os.path.isfile(config_file)
	app.logger.error(
		"Your config.json file is missing." +
        "You need to create one in order for this demo app to run." +
        "Please check the README.md file in order to set it up."
        )
else: 
	app.config.from_json(config_file)

@app.route('/my_key')
def my_key():
    my_config_secret_key = app.config['TWITTER_SECRET_KEY']

    if my_config_secret_key:
        app.logger.debug("Your secret key is: " + my_config_secret_key)
    else:
        app.logger.debug("No SECRET_KEY defined in the config.json")

    return "You should see your secret key in the terminal output"


app.run(debug=True)