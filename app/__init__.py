from flask import Flask

app = Flask(__name__)

# Set the app's secret key
app.config['SECRET_KEY'] = 'based-god'
print(app.config)

from . import routes