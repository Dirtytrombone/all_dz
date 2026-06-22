from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Соси мой хуй"

app.run(port=8000)
