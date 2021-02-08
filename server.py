import subprocess

from flask import Flask, request
from json import dumps, load
import os 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return list_builds()

@app.route('/builds/<id>', methods=['GET'])
def get_build(id):
    f = open(f"./build_details/{id}.json", "r")
    build_details = f.read()
    f.close()

    return build_details


@app.route('/builds', methods=['GET'])
def list_builds():
    interesting_attributes = [
        "commit_id",
        "build_date",
    ]

    # TODO implement
    html = '<html><head>'
    html += '<style>  table, th, td {border: 1px solid black; border-collapse: collapse;}</style>'
    html += "</head><body><H1>Latest Builds</H1><table>"
    
    #open all files in build_details
    arr = os.listdir("build_details")
    first_row_done = False

    for file_name in arr:
        with open("build_details/"+file_name) as json_file:
            data = load(json_file)
            
            if not first_row_done:
                html += "<tr>"
                for key in interesting_attributes:
                    html += f"<th>{key}</th>"
                html += "</tr>"
                first_row_done = True
            
            html += '<tr style="cursor: pointer;" onclick="document.location.href=' + f"'/builds/{file_name[0:-5]}'" + '">'
            for key in interesting_attributes:
                html += f"<td>{data[key]}</td>"
            html += "</tr>"

    html += "</table></body></html>"

    return html


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
