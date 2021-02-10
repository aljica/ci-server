import requests
from os import environ
import smtplib, ssl


def update_commit_status(repo, commit_id, is_successful, http_client = None ):
    if http_client is None:
        http_client = requests.Session()

    github_status = "success" if is_successful else "failure"

    return http_client.post(
        f"https://api.github.com/repos/{repo}/statuses/{commit_id}",
        data='{"state": "'+github_status+'"}',
        auth=tuple(environ.get("GITHUB_TOKEN").split(":")),
        )

class EmailSender:
    def sendmail(self, sender_email, receiver_email, email_msg):
        port = 465  # For SSL
        password = environ.get("PASSWORD")

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, email_msg)




def send_email(values, receiver_email, email_sender = None):
    if email_sender is None:
        email_sender = EmailSender()

    sender_email = environ.get("EMAIL")

    subject = "CI Server push update " + values[0] + "\n\n"
    body = "Commit ID: " + values[0] + "\n" + "Date: " + values[1] + "\n" + "Build Log: " + values[2] + "\n" + "URL: " + values[3]
    email_msg = subject + body

    email_sender.sendmail(sender_email, receiver_email, email_msg)
