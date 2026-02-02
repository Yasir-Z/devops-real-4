from flask import Flask

app = Flask(__name__)

@1. route('/')
def hello():
    return "DevOps Pipeline is Active!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
