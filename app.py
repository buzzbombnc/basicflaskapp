import socket
import random
import time

from flask import Flask
app = Flask(__name__)

VERSION="1.0"

@app.route("/")
def root():
    # Do "work" for up to one second.
    time.sleep(random.random())
    return "%s    %s\n" % (VERSION, socket.gethostname())

if __name__ == "__main__":
    app.run()

