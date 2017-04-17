# Python GitHub Backup
Python script to backup all repositories from a specific user

## How to install
* **Python** (<3) is required. If you have Linux or Mac you should be good to go and you should skip to the next step, if you're on Windows and you like lazy'n'great you can install Python with a couple clicks from: http://ninite.com
* Clone the repository or simply download it as a zip file and unzip it in your local folder
* Customize the variables at the beginning of python-github-backup.py with your data  

### How do I get set up? ###

Following instructions are tested on Raspberry Pi but should work on Debian with no modification and on other distros with minor changes

* Copy / clone this repo into a folder and then add to your:  
`sudo crontab -e`  
this row to run it every 5 minutes:  
`*/5 * * * * /yourpath/network_check.sh`

## How to schedule the script using other Operating Systems  
* If you have Windows: https://technet.microsoft.com/en-us/library/cc748993(v=ws.11).aspx
* If you have Linux or Mac: https://www.howtogeek.com/101288/how-to-schedule-tasks-on-linux-an-introduction-to-crontab-files/

You are now good to go.

## How to use Python GitHub Backup from command line
If you run from command line:    
***python python-github-backup.py***    

Then all the repos for the user specified in the script GITHUB_USER variable will be saved in the folder named in the BACKUP_FOLDER_NAME variable
  
### Contribution guidelines ###

* If you have any idea or suggestion contact directly the Repo Owner

### Who do I talk to? ###

* ltpitt: Repo Owner
