import subprocess

from flask import Flask, request
from json import dumps

app = Flask(__name__)

@app.route('/builds/<id>', methods=['GET'])
def get_build(id):
    f = open(f"./build_details/{id}.json", "r")
    build_details = f.read()
    f.close()

    return build_details


@app.route('/builds', methods=['GET'])
def list_builds(id):
    # TODO implement
    pass


@app.route('/push_hook', methods=['POST'])
def push_hook():
    payload = request.json
    repo = payload['repository']['full_name']
    commit_id = payload['head_commit']['id']
    date = payload['head_commit']['timestamp'].replace("-", "").replace(":","").replace("T", "_")[:-5]

    result = subprocess.run(['sh', './ci.sh', repo, commit_id], stdout=subprocess.PIPE)
    ci_output = str(result.stdout)

    build_details = {
        "commit_id": commit_id,
        "build_date": date,
        "build_logs": ci_output,
        "url": "/builds/"+date
    }
    f = open(f"./build_details/{date}.json", "a")
    f.write(dumps(build_details))
    f.close()
    # TODO save build history

    # TODO send notification to github or email


    return "OK"
