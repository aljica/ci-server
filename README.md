# Continious Integration

This repository contains an implementation of a CI-server. The CI-server follows the following structure:

![CI-server structure](docs/CI_structure.png)
*Image derived from lab instructions*

## Server HTTP API

A description of functions can be found [here](docs/CI_api.md).

## Prerequisities

* Python3
* [Ngrok](https://ngrok.com/download)

**Libraries**

* Python Standard Library 3.9.1
* [Numpy](https://numpy.org)
* [Flask](https://pypi.org/project/Flask/)
  
## Installation 

Install Python3 and the required libraries (`pip3 install numpy` and `pip3 install flask`). 

Download the KTH GitHub repository: <br>
`git clone https://kazaaz:b4c576243990e8768a5aba7a91209435c5aeed4a@github.com/aljica/ci-server.git`

Create a Python3 virtual environment: <br>
`python3 -n venv <name>`

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

`curl -u <GitHubtoken_belonging_to_repository_owner> -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/kazaaz/kth_decide/hooks -d '{"config":{"url":"<NGROK LINK>/push_hook","content_type":"json"}}'`

## Running 
*When working on `kth-decide`:*

Navigate to the branch `assessment`: <br>
`git switch assessment`

Perform and commit changes: <br>
`git add .` <br>
`git commit -m "<Commit message>"` <br>
`git push`

## Testing

Appriopriate unit tests for the CI-server, email-notifications and database have been added and can be found in the `src/builds_test.py`, `src/notification_test.py` and `src/db_test.py` files.

A makefile has been added in order to simplify the process of executing these tests. Thus, the following command can be used to run these tests:

`make test`

## E-mail notifications

You will recieve an e-mail notification when commiting to the repository. This notification contains the information available at `http://<ci_server>/builds` and was implemented following [these](https://realpython.com/python-send-email/) instructions, using the Simple Mail Transfer Protocol (SMTP) found in the `smtplib` module. Furthermore, a Gmail-account was set-up in order to send out e-mails. This account and its password has been safely stored in the `start_server.sh` file. 

Since it is hard to test that an actual message has been delivered via Gmail we decided to mock the `EmailSender` and extract SMTP realted logic to a seperate class. In order to create a fake e-mail and assert that the e-mail is delivered correctly, `unittest.mock` has been used.

## Workflow

**Structure of commit messages**
  
  `feat: description #issue` 

  `fix: decription #issue`

  `test: decription #issue` 

  `enhance: description #issue`

  `documentation: description #issue`

**Statement of contributions**

* Almir Aljic:
  * Implemented functionality for e-mail notifications 
  * Contributed to functionality for connecting and notifying CI-server from GitHub
  * Wrote documentation (incl. internal API)
* Ayham Alkazaz 
  * Implemented functionality for updating GitHub commit status and performed code refactoring, as well as functionality and unit tests for e-mail notifications
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

**Final words**
  
We are proud of the structure, that we managed to follow the naming convension for the commit messages and the collaboration, since all collaborators followed the code of conduct and did their best to follow the workflow that we had set up. Furthermore, we are happy that we managed to plan complete this project within the given time frame. 

## Licence

* BSD 2-Clause License

