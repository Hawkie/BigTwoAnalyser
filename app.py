from flask_wtf.csrf import CSRFProtect
from flask import Flask

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)  # Compliant


@app.route('/')
def hello_world():
    return 'Hello, Docker!'
