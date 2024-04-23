from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    user_input = request.args.get("user_input", "")
    return f'Hello, {escape(user_input)}!'
