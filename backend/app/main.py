import os
from flask import Flask
from dotenv import load_dotenv
from main.routes.api import api

if os.environ.get('DOCKER_RUNNING', 'false') != 'true':
    path = os.getcwd()
    dotenv_path = os.path.dirname(path)
    load_dotenv("{}/.env".format(dotenv_path))

app = Flask(__name__)
app.register_blueprint(api)

@app.route('/')
def index():
    return 'This app is working'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
