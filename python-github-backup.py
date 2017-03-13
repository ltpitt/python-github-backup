import requests
import json
import subprocess
import os

BACKUP_FOLDER_NAME = "backup"
SCRIPT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

BACKUP_FOLDER_PATH = os.path.join(SCRIPT_FOLDER_PATH, BACKUP_FOLDER_NAME)

if not os.path.exists(BACKUP_FOLDER_PATH):
    os.makedirs(BACKUP_FOLDER_PATH)

github_api_response = requests.get("https://api.github.com/users/ltpitt/repos").text
github_api_response = json.loads(github_api_response)

os.chdir(BACKUP_FOLDER_PATH)
[subprocess.call(["git", "clone", item['clone_url']]) for item in github_api_response]
