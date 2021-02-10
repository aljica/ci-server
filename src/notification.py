
import requests
from os import environ


def update_commit_status(repo, commit_id, is_successful):
    github_status = "success" if is_successful else "failure"

    return requests.post(
        f"https://api.github.com/repos/{repo}/statuses/{commit_id}",
        data='{"state": "'+github_status+'"}',
        auth=tuple(environ.get("GITHUB_TOKEN").split(":")),
        )


def send_email():
    # TODO implement
    pass