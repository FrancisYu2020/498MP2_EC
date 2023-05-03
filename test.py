from flask import Flask, request
app = Flask(__name__)
app.seed_for_mp2 = 0

@app.route('/', methods=['POST', 'GET'])
def process_json():
    if request.method == 'POST':
        json = request.json
        app.seed_for_mp2 = json['num']
        return
    elif request.method == 'GET':
        return str(app.seed_for_mp2)
    else:
        raise NotImplementedError

if __name__ == "__main__":
    app.run()
