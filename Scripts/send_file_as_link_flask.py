from flask import Flask, send_file
from pyngrok import ngrok
import sys

file_name = sys.argv[1]
app = Flask(__name__)


@app.route("/<file_name>")
def send(file_name):
    return send_file(file_name)


if __name__ == "__main__":
    url = ngrok.connect(5000)
    print("Link to send: ", url.public_url + "/" + file_name)
    app.run()
