from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def process_json():
    if request.method == 'POST':
        # command to execute
        cmd = "python3 stress_cpu.py"
        # execute command and capture output
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        # read output and wait for command to finish
        out, err = p.communicate()
        # print output
        return out.decode()
    elif request.method == 'GET':
        return socket.gethostname()
    else:
        raise NotImplementedError

if __name__ == "__main__":
    app.run(host='0.0.0.0')
