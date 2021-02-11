# Continuous Integration

This repository contains an implementation of a CI-server.  The CI-server follows the following structure:

![CI-server structure](docs/CI_structure.png)
*Image derived from lab instructions*

## Server HTTP API

A description of functions can be found [here](docs/CI_api.md).

## Prerequisites

* Python3
* [Ngrok](https://ngrok.com/download)

**Libraries**

* Python Standard Library 3.9.1
* [Numpy](https://numpy.org)
* [Flask](https://pypi.org/project/Flask/)
* [Requests](https://pypi.org/project/requests/)
  
## Installation 

Install Python3 and the required libraries (`pip3 install numpy`, `pip3 install flask` and `pip3 install requests`). 

Download the KTH GitHub repository: <br>
`git clone https://<GitHub_name>:<GitHubtoken_belonging_to_someone_who_has_access_to_repository>@github.com/aljica/ci-server.git`

Create a Python3 virtual environment: <br>
`python3 -m venv <name>`

Navigate to the environment: <br>
`cd <name>`

Activate the environment: <br>
`source bin/activate`

Install Python3 dependencies: <br>
`pip3 install -r requirements.txt`

Start the server: <br>
`./start_server.sh`

Download Ngrok, then open a new terminal to unzip the .zip file: <br>
`cd ..` <br>
`cd ..` <br>
`unzip ngrok.zip`

Connect your Ngrok-account: <br>
`./ngrok authtoken <authtoken_belonging_to_your_account>`

Run Ngrok: <br>
`./ngrok http 8006`

Add a new webhook to the repository that you will be working on: <br>

*In this project, we used a copy of the repository for the previous assignment, named `kth-decide`.*

`curl -u <GitHub_name>:<GitHubtoken_belonging_to_repository_owner> -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/kazaaz/kth_decide/hooks -d '{"config":{"url":"<NGROK LINK>/push_hook","content_type":"json"}}'`

## Running 
*When working on `kth-decide`:*

Navigate to the branch `assessment`: <br>
`git switch assessment`

Perform and commit changes: <br>
`git add .` <br>
`git commit -m "<Commit message>"` <br>
`git push`

*When working on other repos:* <br>

Make sure that you have a MakeFile with the following content (in addition to the previous instructions): <br>
`lint:` <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python3 -m pylint --disable C,R,W DECIDE.py && echo "Lint" "OK"`

`test:` <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`python3 DECIDE_test.py && echo "Test" "OK"`

## Testing

Appropriate unit tests for the CI-server, email-notifications and database have been added and can be found in the `src/builds_test.py`, `src/notification_test.py` and `src/db_test.py` files.

A MakeFile has been added in order to simplify the process of executing these tests. Thus, the following command can be used to run these tests:

`make test`

## View documentation in browser

The MakeFile also contains the following command `pydoc3 -b ./` in order to view the entire API as HTML in the browser. Thus, you can obtain the API by using the following command: 

`make doc` 

When running this command, a localhost URL will become visible in the terminal. Paste that link into your browser.

## E-mail notifications

You will receive an e-mail notification when committing to the repository. This notification contains the information available at `http://<ci_server>/builds` and was implemented following [these](https://realpython.com/python-send-email/) instructions, using the Simple Mail Transfer Protocol (SMTP) found in the `smtplib` module. Furthermore, a Gmail-account was set-up in order to send out e-mails. This account and its password has been safely stored in the `start_server.sh` file. 

Since it is hard to test that an actual message has been delivered via Gmail we decided to mock the `EmailSender` and extract SMTP related logic to a separate class. In order to create a fake e-mail and assert that the e-mail is delivered correctly, `unittest.mock` has been used.

## Workflow

**Structure of commit messages**
  
  `feat: description #issue` 

  `fix: description #issue`

  `test: description #issue` 

  `enhance: description #issue`

  `documentation: description #issue`

**Statement of contributions**

*Please note: Pair-programming has been used.*

* Almir Aljic:
  * Implemented functionality for e-mail notifications 
  * Contributed to functionality for connecting and notifying CI-server from GitHub
  * Wrote documentation (incl. internal API)
* Ayham Alkazaz 
  * Implemented functionality for updating GitHub commit status and performed code refactoring, as well as functionality and unit tests for e-mail notifications, implemented build details browser view
  * Created initial project template and contributed to functionality for connecting and notifying CI-server from GitHub
  * Wrote documentation 
* Dina Lerjevik
  * Implemented functionality and unit tests for e-mail notifications 
  * Contributed to functionality for connecting and notifying CI-server from GitHub
  * Wrote documentation (incl. internal API)
* Djiar Salim
  * Implemented initial browser view for the latest builds, functionality for updating GitHub commit status and unit tests for e-mail notifications, performed code refactoring 
  * Contributed to functionality for connecting and notifying CI-server from GitHub
  * Wrote documentation (incl. internal API)
* Sebastian Williams
  * Implemented SQLite database and unit tests for database methods
  * Performed code refactoring
  * Created multiple issues

**Final words**
  
We are proud of the structure, that we managed to follow the naming convention for the commit messages and the collaboration, since all collaborators followed the code of conduct and did their best to follow the workflow that we had set up. Furthermore, we are happy that we managed to plan and complete this project within the given time frame. We are extra proud that we implemented both notification by e-mail and by GitHub commit status, we have also created user-friendly browser view for the build history and build details, additionally we also saved the build history properly in a database.  

## Licence

* BSD 2-Clause License

