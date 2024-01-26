from flask import Flask, request

app = Flask(__name__)
current_seed = 0


@app.route('/', methods=['GET', 'POST'])
def handle_request():
    global current_seed
    if request.method == 'GET':
        return str(current_seed)
    elif request.method == 'POST':
        json_data = request.json
        new_seed= int(json_data['num'])
        current_seed = new_seed
        return "num changed to " + str(current_seed)


if __name__ == '__main__':
    app.run()