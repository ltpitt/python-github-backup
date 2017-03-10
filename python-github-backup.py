import requests
import json
import subprocess

github_api_response = requests.get("https://api.github.com/users/ltpitt/repos").text
github_api_response = json.loads(github_api_response)

for item in github_api_response:
    subprocess.call(["git", "clone", item['clone_url']])
