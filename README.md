# ci-server
Implementation of CI-server

# Installation & start instructions for the CI Server
Create Python3 virtual environment:
> python3 -m venv CI

> cd CI/

Clone ci-server repo
> git clone https://kazaaz:b4c576243990e8768a5aba7a91209435c5aeed4a@github.com/aljica/ci-server.git 

Activate virtualenv:
> source bin/activate

> cd ci-server/src

Install python3 dependencies:
> pip3 install -r requirements.txt

Start the server
> ./start_server.sh 

Open a new terminal & Unzip your ngrok.zip file 
> cd ..
> cd ..
> unzip ngrok.....zip

Run ngrok
> ./ngrok http 8006 

Add a new webhook to kth-decide repo (make sure to copy-paste the correct link!):
> curl -u kazaaz:b4c576243990e8768a5aba7a91209435c5aeed4a -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/kazaaz/kth_decide/hooks -d '{"config":{"url":"<NGROK LINK>/push_hook","content_type":"json"}}'

Test the CI server by pushing something to the branch 'assessment' on kth-decide repo:
> git switch assessment
> nano README.md
*Make changes*
> git add .
> git commit -m . 
> git push

Also, ensure the CI server does not do anything when pushing to the 'master' branch.
