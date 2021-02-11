import subprocess
import db
import notification

def get(id):
    conn = db.create_connection(r"commit_history")
    build_details = db.select_commit(conn, id)

    return build_details

def list():
    conn = db.create_connection(r"commit_history")
    return db.select_all(conn)


def create(payload):
    # Check that the branch is 'assessment'
    if payload['ref'] != "refs/heads/assessment":
        print("Branch is not 'assessment', ignoring.")
        return {}
    repo = payload['repository']['full_name']
    commit_id = payload['head_commit']['id']
    date = payload['head_commit']['timestamp'].replace("-", "").replace(":","").replace("T", "_")[:-5]

    result = subprocess.run(['sh', './ci.sh', repo, commit_id], stdout=subprocess.PIPE)
    ci_output = result.stdout.decode("utf-8")
    lint_successful = ci_output.find("Lint OK") != -1
    test_successful =  ci_output.find("Test OK") != -1

    # Save build history
    build_details = {
        "commit_id": commit_id,
        "build_date": date,
        "build_logs": ci_output,
    }
    values = (commit_id, date, ci_output, "/builds/"+date)
    print(values)
    conn = db.create_connection(r"commit_history")
    with conn:
        db.insert_commit(conn, values)

    # Notification
    is_successful = lint_successful and test_successful
    notification.update_commit_status(repo, commit_id, is_successful)

    # For sending email
    receiver_email = payload['head_commit']['author']['email']
    notification.send_email(values, receiver_email)

    return build_details
