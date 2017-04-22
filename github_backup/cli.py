import click
import requests
import json
import subprocess
import os
import datetime
import shutil
from time import sleep

def create_folders(backup_folder_path, today_backup_folder_path):
    """
    Checks if needed folders exist and, if not, creates them
    """
    folders = [backup_folder_path, today_backup_folder_path]
    for folder in folders:
        if not os.path.exists(folder):
            print "Creating folder: " + folder
            sleep(1)
            os.makedirs(folder)
        else:
            print "Folder already exists: " + folder
            sleep(1)

def get_repository_list_for_specified_user(username):
    """
    Gets complete repository list for specified GitHub username
    """
    print "Getting GitHub repository list for user: " + username
    sleep(1)
    github_api_response = requests.get("https://api.github.com/users/" + username + "/repos").text
    repository_list = json.loads(github_api_response)
    return repository_list

def perform_backup(backup_folder_path, today_backup_folder_path, username):
    """
    Clones all repositories for specified username into today_backup_folder_path
    """
    print "Checking / Creating backup folders..."
    sleep(1)
    create_folders(backup_folder_path, today_backup_folder_path)
    print "Changing current directory to: " + today_backup_folder_path
    sleep(1)
    os.chdir(today_backup_folder_path)
    print "Running git clone of all available repositories for user: " + username
    sleep(1)
    try:
        result = [subprocess.call(["git", "clone", item['clone_url']]) for item in get_repository_list_for_specified_user(username)]
        print "Backup is done, hoorray! :)"
    except OSError as e:
        print "Ouch! Backup threw an error:"
        print e.strerror

def rotate_folders(backup_folder_path, retention_period):
    """
    Deletes all folders in backup_folder_path older than retention_period
    """
    backup_folders_list = os.listdir(backup_folder_path)
    sorted_backup_folders_list = sorted(backup_folders_list)
    if len(sorted_backup_folders_list) > retention_period:
        print "Rotating backup folders and deleting old backups"
        sleep(1)
        folder_to_delete = sorted_backup_folders_list.pop(0)
        folder_to_delete_path = os.path.join(backup_folder_path, folder_to_delete)
        print "Deleting old folder: " + folder_to_delete_path
        sleep(1)
        shutil.rmtree(folder_to_delete_path)
        # Use recursion to delete the oldest folders until the maximum retention period constraint is met
        rotate_folders()

@click.command()
@click.option('--retention-period', '-r', default=3, help='Maximum number of full backups your want to keep, expressed in days (2 will keep, for example, today\'s and yesterday\'s backups and delete the older ones)', required=False)
@click.option('--username', '-u', help='Specify a GitHub username', required=True)
@click.option('--backup-folder-path', '-p', help='Specify the backup folder path', required=True)
def main(retention_period, username, backup_folder_path):
    """GitHub Backup will backup all repositories for the specified user with options for retention"""
    today_backup_folder_path = os.path.join(backup_folder_path, datetime.datetime.now().strftime('%Y%m%d'))
    click.echo('username: ' + username)
    click.echo('backup-folder-path: ' + backup_folder_path)
    click.echo('retention-period: ' + str(retention_period))
    perform_backup(backup_folder_path, today_backup_folder_path, username)
    rotate_folders()

# Uncomment those rows for manual testing
#if __name__ == '__main__':
#    main()