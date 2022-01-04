from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    arquivo = open("templates/home.html")
    return arquivo.read()
