from flask import Flask

app = Flask(__name__)

@app.route('/')  # ✅ FIXED: Changed @1. to @app
def hello():
    return "DevOps Pipeline is Active!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
