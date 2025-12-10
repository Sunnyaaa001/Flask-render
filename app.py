from flask import Flask

app = Flask(__name__)

print("Hello")

@app.route("/")
def index():
    return "Hello"

if __name__ == "__main__":
    app.run()