from flask.app import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'Website Home'


if __name__ == "__main__":
    app.run(debug=True)
