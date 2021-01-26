from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello Nontapat Happy "

if __name__ == "_main_":
    server.run(host='127.0.0.0',port=80)