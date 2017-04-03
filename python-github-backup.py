import requests
import json
import subprocess
import os
import datetime
import shutil
from time import sleep

# Change this variable content with the GitHub username you want to use
GITHUB_USERNAME = "ltpitt"
# If needed also change the backup folder name
BACKUP_FOLDER_NAME = "backup"
# And the maximum number of full backups you want to keep
BACKUP_RETENTION_PERIOD_IN_DAYS = 3

# All the lines below do not need any change
SCRIPT_FOLDER_PATH = os.path.dirname(os.path.abspath(__file__))
BACKUP_FOLDER_PATH = os.path.join(SCRIPT_FOLDER_PATH, BACKUP_FOLDER_NAME)
TODAY_BACKUP_FOLDER_PATH = os.path.join(BACKUP_FOLDER_PATH, datetime.datetime.now().strftime('%Y%m%d'))

def create_folders():
    """
    Checks if needed folders exist and, if not, creates them
    """
    folders = [BACKUP_FOLDER_PATH, TODAY_BACKUP_FOLDER_PATH]
    for folder in folders:
        if not os.path.exists(folder):
            print "Creating folder: " + folder
            sleep(1)
            os.makedirs(folder)
        else:
            print "Folder already exists: " + folder
            sleep(1)

def get_repository_list_for_specified_user():
    """
    Gets complete repository list for specified GITHUB_USERNAME
    """
    print "Getting GitHub repository list for user: " + GITHUB_USERNAME
    sleep(1)
    github_api_response = requests.get("https://api.github.com/users/" + GITHUB_USERNAME + "/repos").text
    repository_list = json.loads(github_api_response)
    return repository_list

def perform_backup():
    """
    Clones all repositories for specified GITHUB_USERNAME into TODAY_BACKUP_FOLDER_PATH
    """
    print "Checking / Creating backup folders..."
    sleep(1)
    create_folders()
    print "Changing current directory to: " + TODAY_BACKUP_FOLDER_PATH
    sleep(1)
    os.chdir(TODAY_BACKUP_FOLDER_PATH)
    print "Running git clone of all available repositories for user: " + GITHUB_USERNAME
    sleep(1)
    try:
        result = [subprocess.call(["git", "clone", item['clone_url']]) for item in get_repository_list_for_specified_user()]
        print "Backup is done, hoorray! :)"
    except OSError as e:
        print "Ouch! Backup threw an error:"
        print e.strerror

def rotate_folders():
    """
    Deletes all folders in BACKUP_FOLDER_PATH older than BACKUP_RETENTION_PERIOD_IN_DAYS
    """
    backup_folders_list = os.listdir(BACKUP_FOLDER_PATH)
    sorted_backup_folders_list = sorted(backup_folders_list)
    if len(sorted_backup_folders_list) > BACKUP_RETENTION_PERIOD_IN_DAYS:
        print "Rotating backup folders and deleting old backups"
        sleep(1)
        folder_to_delete = sorted_backup_folders_list.pop()
        folder_to_delete_path = os.path.join(BACKUP_FOLDER_PATH, folder_to_delete)
        print "Deleting old folder: " + folder_to_delete_path
        sleep(1)
        shutil.rmtree(folder_to_delete_path)

# Let's rock :)      
perform_backup()
rotate_folders()
