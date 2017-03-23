import requests
import json
import subprocess
import os

GITHUB_USERNAME = "ltpitt"
BACKUP_FOLDER_NAME = "backup"
SCRIPT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))

BACKUP_FOLDER_PATH = os.path.join(SCRIPT_FOLDER_PATH, BACKUP_FOLDER_NAME)

if not os.path.exists(BACKUP_FOLDER_PATH):
    os.makedirs(BACKUP_FOLDER_PATH)

github_api_response = requests.get("https://api.github.com/users/" + GITHUB_USERNAME + "/repos").text
github_api_response = json.loads(github_api_response)

os.chdir(BACKUP_FOLDER_PATH)

try:
    result = [subprocess.call(["git", "clone", item['clone_url']]) for item in github_api_response]
    print "Backup is done, hoorray! :)"
except OSError as e:
    print "Ouch! Backup threw an error:"
    print e.strerror
