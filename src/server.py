from flask import Flask, request
import db
import builds

app = Flask(__name__)

@app.before_request
def before_request():
    """Initializes database

    Parameters:
    None
    
    Return:
    None
    """    
    db.init()

@app.route('/', methods=['GET'])
def ping():
    """Lists builds

    Parameters:
    None
    
    Return:
    builds (str): String representative of commit history
   """    
    builds = list_builds()
    return builds


@app.route('/builds/<id>', methods=['GET'])
def get_build(id):    
    """Returns build details

    Parameters:
    id (str): Commit ID (sha-hash)
    
    Return:
    build_details (str): String representative of commit information
   """    
    build_details = builds.get(id)
    return build_details


@app.route('/builds', methods=['GET'])
def list_builds():
    """Lists the commit history formatted as a string representative of an HTML document

    Parameters:
    None

    Returns:
    html (str): String representative of commit history in HTML. The commits are listed in a table
   """
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
    """Extracts key/relevant information from payload, runs tests, inserts commit info into database, notifies whether (un)successful and sends e-mail to author of commit

    Parameters:
    None

    Returns:
    ok (str): Approving message as a string
   """
    payload = request.json

    builds.create(payload)

    ok = "OK"
    return ok
