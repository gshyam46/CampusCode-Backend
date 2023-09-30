from flask import Flask
from routes.sample import sample_bp


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Campus Code!'


app.register_blueprint(sample_bp, url_prefix='/api')

app.debug = True
if __name__ == "__main__":
    app.run(debug=True)