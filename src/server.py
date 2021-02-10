from flask import Flask, request
import db
import builds

app = Flask(__name__)

@app.before_request
def before_request():
    db.init()

@app.route('/', methods=['GET'])
def ping():
    return list_builds()


@app.route('/builds/<id>', methods=['GET'])
def get_build(id):
    return builds.get(id)


@app.route('/builds', methods=['GET'])
def list_builds():
    commit_array = builds.list()

    interesting_attributes = [
        "commit_id",
        "build_date",
    ]

    # TODO implement
    html = '<html><head>'
    html += '<style>  table, th, td {border: 1px solid black; border-collapse: collapse;}</style>'
    html += "</head><body><H1>Latest Builds</H1><table>"

    html += "<tr>"
    for key in interesting_attributes:
        html += f"<th>{key}</th>"
    html += "</tr>"

    for commit in commit_array:
        html += '<tr style="cursor: pointer;" onclick="document.location.href=' + f"'/builds/{commit[0]}'" + '">'
        for key in range(2):
            html += f"<td>{commit[key]}</td>"
        html += "</tr>"

    html += "</table></body></html>"

    return html


@app.route('/push_hook', methods=['POST'])
def push_hook():
    payload = request.json

    builds.create(payload)

    return "OK"
