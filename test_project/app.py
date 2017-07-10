from flask import Flask
from api.division import division_api

from config import Config

app = Flask(__name__)

app.register_blueprint(division_api)


if (__name__ == "__main__"):
	app.run(host='0.0.0.0', port=Config.port, debug=True)