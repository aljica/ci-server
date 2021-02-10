import requests
from os import environ
import smtplib, ssl

def update_commit_status(repo, commit_id, is_successful):
    github_status = "success" if is_successful else "failure"

    return requests.post(
        f"https://api.github.com/repos/{repo}/statuses/{commit_id}",
        data='{"state": "'+github_status+'"}',
        auth=tuple(environ.get("GITHUB_TOKEN").split(":")),
        )


def send_email(values, receiver_email):
    port = 465  # For SSL
    sender_email = environ.get("EMAIL")
    password = environ.get("PASSWORD")

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)

        subject = "CI Server push update " + values[0] + "\n\n"
        body = "Commit ID: " + values[0] + "\n" + "Date: " + values[1] + "\n" + "Build Log: " + values[2] + "\n" + "URL: " + values[3]
        email_msg = subject + body

        server.sendmail(sender_email, receiver_email, email_msg)
