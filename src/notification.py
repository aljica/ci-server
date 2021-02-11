import requests
from os import environ
import smtplib, ssl


def update_commit_status(repo, commit_id, is_successful, http_client = None ):
    """Updates the commit status for the specific commit according to the parameter is_successful by executing a POST

    Parameters:
    repo (str): The name of the repo
    commit_id (str): Commit ID (sha-hash)
    is_successful (bool): The new status for the commit. True for successful, false otherwise
    http_client (requests.Session): The Session object. If not provided, a new Session object will be created

    Returns:
    response (requests.Response): A Response object
   """    
    if http_client is None:
        http_client = requests.Session()

    github_status = "success" if is_successful else "failure"

    response = http_client.post(
        f"https://api.github.com/repos/{repo}/statuses/{commit_id}",
        data='{"state": "'+github_status+'"}',
        auth=tuple(environ.get("GITHUB_TOKEN").split(":")),
        )
    
    return response

class EmailSender:
    """ A class for sending e-mails

    Attributes
    ----------
    None

    Methods
    ----------
    sendmail(sender_email, receiver_email, email_msg):
        Sends an e-mail with the provided content. The environment variable PASSWORD has to be set for the sender's e-mail account
    
   """
    def sendmail(self, sender_email, receiver_email, email_msg):
        """Sends an e-mail with the provided content. The environment variable PASSWORD has to be set for the sender's e-mail account

        Parameters:
        sender_email (str): The sender's e-mail adress 
        receiver_email (str): The receiver's e-mail adress
        email_msg (str): The content of the e-mail message

        Returns:
        None
       """        
        port = 465  # For SSL
        password = environ.get("PASSWORD")

        # Create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, email_msg)




def send_email(values, receiver_email, email_sender = None):
    """Creates an EmailSender object and sends a formatted version of the commit attributes to the receiver through e-mail

    Parameters:
    values (tuple): The build details of a commit
    receiver_email (str): The receiver's e-mail adress
    email_sender (EmailSender): The EmailSender object which is used to send the e-mail. If not provided, a new EmailSender object will be created with environment variable EMAIL

    Returns:
    None
   """    
    if email_sender is None:
        email_sender = EmailSender()

    sender_email = environ.get("EMAIL")

    subject = "CI Server push update " + values[0] + "\n\n"
    body = "Commit ID: " + values[0] + "\n" + "Date: " + values[1] + "\n" + "Build Log: " + values[2] + "\n" + "URL: " + values[3]
    email_msg = subject + body

    email_sender.sendmail(sender_email, receiver_email, email_msg)
