import unittest
from unittest import mock
import notification
from unittest.mock import Mock
from os import environ

class TestNotification(unittest.TestCase):
    def test_update_commit_status_sends_http_success_status(self):
        github_auth = tuple(environ.get("GITHUB_TOKEN").split(":"))
        repo = "test/hello_world"
        commit_id = "04dbec97248ca15f8db8567efbe48b3b2e85a32e"
        mock_client = Mock()

        notification.update_commit_status(repo, commit_id, True, http_client=mock_client)
        mock_client.post.assert_called_with('https://api.github.com/repos/test/hello_world/statuses/04dbec97248ca15f8db8567efbe48b3b2e85a32e', auth=github_auth, data='{"state": "success"}')

    def test_update_commit_status_sends_http_failure_status(self):
        github_auth = tuple(environ.get("GITHUB_TOKEN").split(":"))
        repo = "test/hello_world"
        commit_id = "04dbec97248ca15f8db8567efbe48b3b2e85a32e"
        mock_client = Mock()

        notification.update_commit_status(repo, commit_id, False, http_client=mock_client)
        mock_client.post.assert_called_with('https://api.github.com/repos/test/hello_world/statuses/04dbec97248ca15f8db8567efbe48b3b2e85a32e', auth=github_auth, data='{"state": "failure"}')


    def test_send_email_sends_build_details(self):
        sender_email = environ.get("EMAIL")

        commit_id = "04dbec97248ca15f8db8567efbe48b3b2e85a32e"
        date = "20200121"
        logs = "Building ... Testing ..."
        url = "/builds/"+commit_id


        values = [
            commit_id, date, logs, url
        ]
        receiver_email = "test@example.com"

        mock_email_server = Mock()

        notification.send_email(values, receiver_email, email_sender= mock_email_server)

        mock_email_server.sendmail.assert_called_with(sender_email, receiver_email, 'CI Server push update 04dbec97248ca15f8db8567efbe48b3b2e85a32e\n\nCommit ID: 04dbec97248ca15f8db8567efbe48b3b2e85a32e\nDate: 20200121\nBuild Log: Building ... Testing ...\nURL: /builds/04dbec97248ca15f8db8567efbe48b3b2e85a32e')




if __name__ == '__main__':
    unittest.main()

