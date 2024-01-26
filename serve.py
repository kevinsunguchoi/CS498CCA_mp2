import subprocess
import socket
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        return socket.gethostname()
    elif request.method == 'POST':
        process = subprocess.Popen(["python3", "stress_cpu.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return "post complete"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)