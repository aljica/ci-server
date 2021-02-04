from flask import Flask, request

app = Flask(__name__)

@app.route('/builds/<id>', methods=['GET'])
def get_build(id):
    # TODO implement
    pass


@app.route('/builds', methods=['GET'])
def list_builds(id):
    # TODO implement
    pass


@app.route('/push_hook', methods=['POST'])
def push_hook():
    payload = request.get_json(silent=True)
    print(payload)
    # TODO build & test

    # TODO send notification to github or email

    # TODO save build history

    return "OK"
