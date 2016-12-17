import socket

from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "Greetings from server %s\n" % socket.gethostname()

if __name__ == "__main__":
    app.run()

