# Continous Integration - Server HTTP API

## Explanation of functions

See the code for more code-specific method documentation regarding e-mail notifications etc. Furthermore, the following command can be used to view the API of a file (e.g. `server.py`) as a HTML file: 

`pydoc -w ./<filename>`

## Get build information 

In order to obtain build details about a specific commit, send a GET HTTP-request to `http://<ci_server>/builds/<id>`, where <`id`> is to be replaced with the requested commit ID. 

It is also possible to obtain build details by accessing the web view for the build history list (as mentioned in the following section) and clicking on the specific build of interest.

## List build history

An overview over all previous builds can be found at `http://<ci_server>/builds`

## Github webhook

The CI-server listens to git push events broadcasted by GitHub at the following URL: `http://<ci_server/push_hook`. The URL should be encoded as `json`. This should be configured as a webhook in GitHub.


