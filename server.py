import subprocess
import sqlite3

from flask import Flask, request
from json import dumps, load
from sqlite3 import Error
import os 

app = Flask(__name__)

def create_connection(db_file):
    # Create a database connection to a SQLite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    # Create the build_history table
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_commit(conn, commit):
    """
    Create a new task
    :param conn: DB connection
    :param task: {id, date, logs, url}
    :return:
    """

    sql = ''' INSERT INTO history(commit_id,build_date,build_logs,url)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, commit)
    conn.commit()

    return cur.lastrowid


def select_commit(conn, id):
    # Select commit by id
    cur = conn.cursor()
    cur.execute("SELECT * FROM history WHERE commit_id=?", (id,))

    row = cur.fetchone()
    build_details = {
        "commit_id": row[0],
        "build_date": row[1],
        "build_logs": row[2],
        "url": row[3]
    }
    return build_details


def select_all(conn):
    # Select commit by id
    cur = conn.cursor()
    cur.execute("SELECT * FROM history")

    rows = cur.fetchall()
    return rows

sql_create_build_history_table = """CREATE TABLE IF NOT EXISTS history (
                                    commit_id text PRIMARY KEY,
                                    build_date text NOT NULL,
                                    build_logs text NOT NULL,
                                    url text NOT NULL
                                );"""


@app.before_request
def before_request():
    conn = create_connection(r"commit_history")
    if conn is not None:
        create_table(conn, sql_create_build_history_table)
    else:
        print("Error! cannot create the database connection.")


@app.route('/', methods=['GET'])
def ping():
    return list_builds()


@app.route('/builds/<id>', methods=['GET'])
def get_build(id):
    conn = create_connection(r"commit_history")
    build_details = select_commit(conn, id)

    return build_details


@app.route('/builds', methods=['GET'])
def list_builds():
    interesting_attributes = [
        "commit_id",
        "build_date",
    ]

    conn = create_connection(r"commit_history")
    commit_array = select_all(conn)

    # TODO implement
    html = '<html><head>'
    html += '<style>  table, th, td {border: 1px solid black; border-collapse: collapse;}</style>'
    html += "</head><body><H1>Latest Builds</H1><table>"

    html += "<tr>"
    for key in interesting_attributes:
        html += f"<th>{key}</th>"
    html += "</tr>"

    for commit in commit_array:
        html += '<tr style="cursor: pointer;" onclick="document.location.href=' + f"'/builds/{commit[1]}'" + '">'
        for key in range(2):
            html += f"<td>{commit[key]}</td>"
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

    # Save build history
    build_details = {
        "commit_id": commit_id,
        "build_date": date,
        "build_logs": ci_output,
        "url": "/builds/"+date
    }
    values = (commit_id, date, ci_output, "/builds/"+date)
    print(values)
    conn = create_connection(r"commit_history")
    with conn:
        insert_commit(conn, values)
    # f = open(f"./build_details/{date}.json", "a")
    # f.write(dumps(build_details))
    # f.close()
    # TODO send notification to github or email


    return "OK"
