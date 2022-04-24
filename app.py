
from datetime import date
from flask.templating import render_template 
import config

from flask import Flask
app = Flask("Web page to Display current time and data")
app.config.from_object(config)
print(app.config)

@app.route('/')

def home():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(port = config.PORT, debug = config.DEBUG)
    today = home()