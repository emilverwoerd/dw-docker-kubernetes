import time
import socket

from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    server = socket.gethostname()
    return 'Hello World! on pc: ' + server

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)