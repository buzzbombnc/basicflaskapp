import socket

from flask import Flask
app = Flask(__name__)

VERSION="1.0"

@app.route("/")
def root():
    return "%s    %s" % (VERSION, socket.gethostname())

if __name__ == "__main__":
    app.run()

