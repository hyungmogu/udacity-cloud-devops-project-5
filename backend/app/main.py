from flask import Flask
from dotenv import load_dotenv
from main.routes.api import api

load_dotenv()

app = Flask(__name__)
app.register_blueprint(api)

@app.route('/')
def index():
    return 'This app is working'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
