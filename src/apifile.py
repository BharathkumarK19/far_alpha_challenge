from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello')
def say_hello():
    return jsonify({"message": "Hello User!"})

@app.route('/')
def index():
    return "Welcome to the homepage!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)