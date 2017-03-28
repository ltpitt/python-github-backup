# Python GitHub backup
Python script to backup all repositories from a specific user

## How to install
* **Python** (<3) is required. If you have Linux or Mac you should be good to go and you should skip to the next step, if you're on Windows and you like lazy'n'great you can install Python with a couple clicks from: http://ninite.com
* Clone the repository or simply download it as a zip file and unzip it in your local folder
* If you have **pip** skip to next step. You need **pip** to easily install requirements, if you do not have **pip** you can install it using this tutorial: https://pip.pypa.io/en/latest/installing.html 
* Customize the variables at the beginning of python-github-backup.py with your data
* Run this command (be sure to run it from python-github-backup.py folder) to install requirements: ***pip install -r requirements.txt***

## How to schedule the script  
* If you have Windows: https://technet.microsoft.com/en-us/library/cc748993(v=ws.11).aspx
* If you have Linux or Mac: https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/

You are now good to go.

## How to use simple_notifications.py from command line
If you run from command line:    
***python python-github-backup.py***    

Then all the repos for the user specified in the script GITHUB_USER variable will be saved in the folder named in the BACKUP_FOLDER_NAME variable
  
### Contribution guidelines ###

* If you have any idea or suggestion contact directly the Repo Owner

### Who do I talk to? ###

* ltpitt: Repo Owner
